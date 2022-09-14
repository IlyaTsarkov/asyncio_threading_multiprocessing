import concurrent.futures
import random
import time
from functools import wraps


def how_long(func):
    """Декоратор для измерения времени"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Выполнено за {end - start} секунд')
        return res

    return wrapper


def write_in_file(n, filename):
    """Функция для записи в файл 3000000 трехзначных чисел"""
    print('start write')
    with open(filename, 'w') as file:
        while n <= 3000000:
            file.write(str(random.randint(1, 1000)) + '\n')
            n += 1

    print('end write')


@how_long
def example_with_threads():
    """Запись 3000000 чисел в два файла, используя "параллельные" потоки"""
    print('Старт потока example_with_threads()')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(write_in_file, 1, 'example1.txt')
        executor.submit(write_in_file, 1, 'example2.txt')

    print('Конец потока example_with_threads()', '\n', sep='')


@how_long
def example_without_threads():
    """Запись 3000000 чисел в два файла, используя последовательные потоки"""
    print('Старт потока example_without_threads()')
    write_in_file(1, 'example3.txt')
    write_in_file(1, 'example4.txt')
    print('Конец потока example_without_threads()')


if __name__ == '__main__':
    # Запуск Foreground потока
    print('Старт потока main()')
    # Запуск программы, которая использует "Параллельные" потоки
    example_with_threads()
    # Запуск программы, которая использует Последовательные потоки
    example_without_threads()
    print('Конец потока main()')
