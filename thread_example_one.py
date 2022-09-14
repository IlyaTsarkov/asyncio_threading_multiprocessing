import time
import threading


def long_def(n, x):
    """Программа, которая выполняется не мгновенно"""
    start = time.time()
    lst = []
    while n <= x:
        lst.append(n)
        n += 1

    end = time.time()
    print(f'Выполнено за {end - start}\nЗначение - {sum(lst)}')


if __name__ == '__main__':
    # Точка входа в программу, по умолчанию главный поток
    print('Запуск потока main()')

    # Создаем поток, по умолчанию создан Foreground поток и теперь
    # Это главный поток, или вернее сказать тоже
    thread = threading.Thread(target=long_def, args=(1, 30000000), daemon=True)
    # Запускаем поток
    thread.start()
    # Говорим, что пока этот поток работает программа не должна завершаться
    thread.join()

    print('Завершение потока main()')
    # thread.join()
    # В таком случае сначала мы увидим строку
    # 'Завершение потока main()'
    # И после нее начнется выполнение потока thread
