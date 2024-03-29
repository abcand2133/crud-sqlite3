from crud import UserCRUD
from db import DBConnection


db_obj = DBConnection(db_name='todos.db')

user_crud = UserCRUD()

commands = ["1. get", "2. create", "3. update", "4. delete"]
commands_text = "\n".join(commands)
while True:
    work_with = input('users, todos[]\nВыберите из списка: ')
    if work_with == 'users':
        user_command = input(f'{commands_text}\nВыберите номер команды: ')
        if user_command == "1":
            print('get method')
            command_get = input('1. Get one by username\n2. Get all\nВыберите номер: ')
            if command_get == "1":
                print('usernames')
                users = user_crud.get_all(db_obj)
                usernames = [f"{idx}. {username}" for idx, (_, username) in enumerate(users, start=1)]
                usernames_text = "\n".join(usernames)
                name = input(f'{usernames_text}\nНапишите имя пользователя: ')
                user = user_crud.get(db_obj, name)
                if isinstance(user, tuple):
                    print(f'Получили пользователя:\nID: {user[0]}\nUSERNAME: {user[1]}')
                else:
                    print('Пользователь не найден')


            elif command_get == "2":
                print("all users data")
                users = user_crud.get_all(db_obj)
                user_count = 1
                for user_id, username in users:
                    print(f'==============\n{user_count}. ID: {user_id}\nUSERNAME: {username}\n==============')
                    user_count += 1

        elif user_command == "2":
            print('create method')
            username = input('Введите имя пользователя: ')
            user = user_crud.create(db=db_obj, value=username)
            if isinstance(user, tuple):
                print(f'Создали пользователя:\nID: {user[0]}\nUSERNAME: {user[1]}')
            elif isinstance(user, str):
                print(user)

        elif user_command == "3":
            print('update method')

        elif user_command == "4":
            print('delete method')
