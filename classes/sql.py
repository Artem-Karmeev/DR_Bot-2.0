from config import cursor, connect
import uuid


class BData():

    users_id = {}
    user_data = {}


    def __init__(self) -> None:

        cursor.execute("SELECT * FROM users_flags")
        data = cursor.fetchall()
        self.users_id = {data[i][0]: data[i][1] for i in range(len(data))}
        connect.commit()
        print('Connection.')


    def get_user(self, user_data: tuple):

        """Добавит пользователя в бд, установит флаг '1'
        в user_data ожидается: user_id, user_name, full_name"""

        self.users_id[user_data[0]] = 1
        value = (user_data[0], 1, )
        cursor.execute("INSERT INTO users_flags VALUES(?, ?)", value)
        cursor.execute("INSERT INTO users VALUES(?, ?, ?);", user_data)
        connect.commit()


    def get_event(self, user_id: int, user_event: tuple):

        """Добавит событие в бд. В users_events ожидается:
        data, comment"""

        id = str(uuid.uuid4())
        event = (id, user_id, ) + user_event
        cursor.execute("INSERT INTO users_events VALUES(?, ?, ?, ?)", event)
        connect.commit()


    def fill_data(self, user_id: int):
        """"""
        cursor.execute(f"SELECT date, comment, id FROM users_events WHERE user_id = {user_id}")
        data = cursor.fetchall()
        data = [list(data[i]) for i in range(len(data))]
        data = sorted(data, key=lambda x: (int(x[0].split('.')[1]), int(x[0].split('.')[0]))) 
        connect.commit()
        self.user_data[user_id] = data


    def show(self, user_id: int) -> str:
        """"""
        result = ''
        for i in range(len(self.user_data[user_id])):
            result += f'🆔: {i} 📆: {self.user_data[user_id][i][0]} 📝: {self.user_data[user_id][i][1]}\n'
        return result


    def search(self, user_id: int, search: str) -> str:
        """"""
        result = ''
        for i in range(len(self.user_data[user_id])):
            if search in self.user_data[user_id][i][0].lower() \
                or search in self.user_data[user_id][i][1].lower():
                result += f'🆔: {i} 📆: {self.user_data[user_id][i][0]} 📝: {self.user_data[user_id][i][1]}\n'
        return result


    def del_event(self, user_id: int, index: int):
        """"""
        cursor.execute(f"DELETE FROM users_events WHERE id = '{self.user_data[user_id][index][2]}'")
        connect.commit()


    def switch(self, user_id: int):
        """"""
        flag = 0 if self.users_id[user_id] else 1
        self.users_id[user_id] = flag
        cursor.execute('''UPDATE users_flags SET flag = ? WHERE user_id = ?''', (flag, user_id))
        connect.commit()
        return flag


    def check(self, user_id) -> bool:
        """Вернет наличие id в словаре"""
        return user_id in self.users_id
    

    def len(self, user_id: int):
        """Вернет длину данных пользователя"""
        return len(self.user_data[user_id])


    def clear(self, user_id: int): 
        """Удалит данные пользователя из оперативной памяти"""
        if user_id in self.user_data:
            self.user_data.pop(user_id)

    
    def return_flag(self, user_id: int):
        """Вернет влаг пользователя"""
        return self.users_id[user_id]
    

