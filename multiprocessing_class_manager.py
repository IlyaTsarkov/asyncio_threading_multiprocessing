import multiprocessing
import random


class ExManager:
    def __init__(self, n):
        self.n = n

    # Изменяем объект менеджера из другого процесса
    def list_append(self, m_list):
        m_list.append(self.n)


if __name__ == '__main__':
    # Случайное число и передача его в качестве аргумента
    rand_number = random.randint(1, 30)
    ex_m = ExManager(rand_number)

    # Запуск процессов в качестве менеджеров
    processes = []
    with multiprocessing.Manager() as manager:
        # Менеджер поддерживает разные типы данных, например воспользуемся списком
        manager_list = manager.list()
        print(f'До работы - {manager_list}')
        # Два процесса будут влиять на список
        for _ in range(2):
            pr = multiprocessing.Process(target=ex_m.list_append, args=(manager_list,))
            processes.append(pr)
            pr.start()

        [process.join() for process in processes]

        # Вывод итогового списка
        print(f'После работы - {manager_list}')
