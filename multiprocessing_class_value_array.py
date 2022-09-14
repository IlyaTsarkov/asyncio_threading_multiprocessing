import multiprocessing
import random


class DigitWorks:
    def __init__(self, number):
        self.number = number
        # Lock(), поскольку участвуют несколько процессов
        self.locker = multiprocessing.Lock()

    def count_of_process(self, d_array, n):
        cur_pr = multiprocessing.current_process().pid
        # Используем Lock()
        with self.locker:
            # Добавляем id процесса в массив
            d_array[n] = cur_pr

    @staticmethod
    def calculations(d_value):
        """Статический метод для проверки Value на четность"""
        print(f'\nЧисло - {d_value}')
        if d_value % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')


if __name__ == '__main__':
    rand_number = random.randint(1, 5)
    ex = DigitWorks(rand_number)
    # Создаем объекты Array() и Value()
    array = multiprocessing.Array('i', rand_number)
    value = multiprocessing.Value('d', rand_number)

    print(f'Работаем в - {multiprocessing.current_process().name}')

    # Value() будем использовать один раз внутри процесса
    pr_for_value = multiprocessing.Process(target=ex.calculations, args=(rand_number,))
    pr_for_value.start()
    pr_for_value.join()

    # Array() будем использовать несколько раз внутри разных процессов
    process = []
    for i in range(rand_number):
        pr = multiprocessing.Process(target=ex.count_of_process, args=(array, i))
        process.append(pr)
        pr.start()

    [proc.join() for proc in process]

    # Вывод итоговых результатов
    print(f'\nСписок id процессов - {list(array)}'
          f'\nКоличество процессов - {len(list(array))}')
