import random
import string
import threading
import time


class ListOfUsers:
    """Класс для хранения списка пользователей"""
    def __init__(self):
        # Устанавливаем список начальных пользователей
        self.list_of_names = ['vova', 'jora']
        self.locker = threading.Lock()

    def new_name(self, user_name: str):
        """Функция для добавления нового пользователя"""
        # Блокируем доступ для остальных потоков пока фрагмент кода занят
        self.locker.acquire()
        print(f'Новый пользователь - {user_name}')
        # Имитируем задержку добавления для провоцирования context switch
        time.sleep(2)
        self.locker.acquire()
        self.list_of_names.append(user_name)
        print(f'Пользователь {user_name} добавлен')

        print(f'Список пользователей после - {lock_example.list_of_names}')
        self.locker.release()


if __name__ == '__main__':
    # Создаем экземпляр и показываем начальный список
    lock_example = ListOfUsers()
    print(f'Список пользователей в начале - {lock_example.list_of_names} ')

    # Забираем в переменную alphabets все буквы
    alphabets = string.ascii_letters
    # Три раза формируем разное случайное имя и выделяем 3 потока на добавление
    # их в список с помощью метода new_name()
    for _ in range(3):
        new_name = ''.join(random.choice(alphabets) for i in range(random.randint(2, 5)))
        threading.Thread(target=lock_example.new_name, args=[new_name]).start()

# users = {}
# users_count = 0
#
#
# def new_user(name, password):
#     global users
#     global users_count
#     for i in range(1):
#         users[name] = password
#         print(users)
#         users_count += 1
#         print(users_count)
#
#
# if __name__ == '__main__':
#     alphabets = string.ascii_letters
#     alphabets_and_digits = string.ascii_letters + string.digits
#     for user in range(5000):
#         new_name = ''.join(random.choice(alphabets) for i in range(random.randint(3, 6)))
#         new_password = ''.join(random.sample(alphabets_and_digits, random.randint(6, 9)))
#         threading.Thread(target=new_user, args=(new_name, new_password)).start()
