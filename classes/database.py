from config import link_db
import sqlite3 
import uuid
from aiogram.types import Message as mg

class UserData:

    connect = None
    cursor = None

    message: mg = None 
    # user_id = None

    stat = True
    flag = None
    events = None

    def __init__(self, message: mg, load_events: bool = False, link_database: str = link_db):

        self.connect = sqlite3.connect(link_database)
        self.cursor = self.connect.cursor()
        
        self.message = message

        self.cursor.execute("SELECT flag FROM users WHERE id = ?", (message.from_user.id, ))
        result = self.cursor.fetchone()

        if result == None:

            user_data = (message.from_user.id, message.from_user.username, message.from_user.full_name, 1, )
            self.cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user_data)
            self.connect.commit()
            self.flag = 1
            self.stat = False

        else:
            self.flag = result[0]

        if load_events:
            self.cursor.execute(f"SELECT date, comm, id FROM events WHERE user_id = ?", (message.from_user.id, ))
            data = self.cursor.fetchall()
            data = [list(data[i]) for i in range(len(data))]
            data = sorted(data, key=lambda x: (int(x[0].split('.')[1]), int(x[0].split('.')[0]))) 
            self.events = data


    def new_event(self, event: tuple):

        """Добавит событие в бд. В users_events ожидается:
        data, comment"""

        id = str(uuid.uuid4())
        event = (id, self.message.from_user.id, ) + event
        self.cursor.execute("INSERT INTO events VALUES(?, ?, ?, ?)", event)
        self.connect.commit()
        self.connect.close()


    def del_event(self, index: int) -> str:

        """Удалит событие пользователя из бд
        вернет строку для отправки пользователю """

        if -1 < index < len(self.events):
            self.cursor.execute("DELETE FROM events WHERE id = (?)", (self.events[index][2], ))
            self.connect.commit()
            self.connect.close()
            return 'Событие удалено.'
        else:
            return 'ERROR: "ID".'


    def switch(self):

        """Изменит флаг"""

        flag = 0 if self.flag else 1
        self.cursor.execute('''UPDATE users SET flag = ? WHERE id = ?''', (flag, self.message.from_user.id))
        self.connect.commit()
        self.connect.close()


    def show(self) -> str:

        """ Вернет строку с событиями пользователя """

        result = ''
        for i in range(len(self.events)):
            result += f'🆔: {i} 📆: {self.events[i][0]} 📝: {self.events[i][1]}\n'
        self.cursor.close()
        return result


    def check_flag(self) -> int:

        """Вернет флаг пользователя"""

        self.cursor.close()
        return self.flag
    

    def check_in_db(self):
        """ """
        self.cursor.close()
        return self.stat