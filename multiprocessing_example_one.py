import multiprocessing
import random
import string
import os
import time


class ListOfUsers:
    """Класс для хранения списка пользователей"""

    def __init__(self):
        # Устанавливаем список начальных пользователей
        self.users = {}
        # Добавим экземпляр Lock()
        self.locker = multiprocessing.Lock()

    def new_user(self, name, password, queue):
        # Добавление нового пользователя в словарь.
        # Используем блокировку, чтобы
        with self.locker:
            self.users[name] = password

            # Вывод информации о процессе
            print(f'\nid процесса: {os.getpid()}'
                  f'\nРодительский процесс - {os.getppid()}'
                  f'\nИмя процесса - {multiprocessing.current_process().name}')

            # Вывод пользователей после работы метода внутри процесса
            queue.put(self.users)
            print(self.users)
            time.sleep(0.4)


if __name__ == '__main__':
    # Экземпляр класса
    ex_list = ListOfUsers()
    # Экземпляр очереди
    q = multiprocessing.Queue()
    # Переменная со всеми буквами, для генерации имени
    alphabets = string.ascii_letters
    # Переменная со всеми буквами + цифрами, для генерации пароля
    alphabets_and_digits = string.ascii_letters + string.digits

    # Информация до начала работы
    print(f'Словарь пользователей вначале - {ex_list.users}\n'
          f'Количестве ядер процессора устройства - {multiprocessing.cpu_count()}')

    # Список для хранения потоков
    processes_list = []
    # Генерация имен, паролей и запуск .new_user() с этими данными в разных процессах
    for process in range(3):
        new_name = ''.join(random.choice(alphabets) for i in range(random.randint(3, 6)))
        new_password = ''.join(random.sample(alphabets_and_digits, random.randint(6, 9)))
        new_process = multiprocessing.Process(target=ex_list.new_user, args=(new_name, new_password, q), daemon=True)
        # Добавление каждого нового процесса в список processes_list
        processes_list.append(new_process)
        new_process.start()

    # Применяем .join() к каждому процессу
    for i in processes_list:
        i.join()

    # Метод .get() извлекает объект из очереди, если очередь закрыта - вызывается ValueError
    print('\nФормируем словарь пользователей из данных, которые хранятся в очереди')
    new_users_dict = {}
    try:
        for obj in iter(q.get_nowait, None):
            new_users_dict.update(obj)
    except Exception:
        print(f'Итоговый словарь - {new_users_dict}')


