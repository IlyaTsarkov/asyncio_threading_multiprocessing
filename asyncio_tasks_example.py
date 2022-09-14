import asyncio


async def simple_msg(text):
    """Простой корутин, который возвращает текст"""
    print(text)


async def count(x):
    """Простой корутин, который возвращает количество битов"""
    print(x.bit_count())


async def long_operation(msg):
    """Корутин с большой задержкой"""
    print(f'Старт задачи {msg}')
    await asyncio.sleep(3)
    print(f'Конец задачи {msg}')


async def main():
    """Функция, в которой проверяем важен ли
    порядок вывода корутин"""

    # Работа двух мгновенных корутин
    short_task_11 = asyncio.create_task(simple_msg('Сообщение 1'))
    short_task_12 = asyncio.create_task(count(10))

    # Работа корутина с задержкой
    long_task_one = asyncio.create_task(long_operation('Задача 1'))
    long_task_two = asyncio.create_task(long_operation('Задача 2'))

    # Работа двух мгновенных корутин
    short_task_21 = asyncio.create_task(simple_msg('Сообщение 2'))
    short_task_22 = asyncio.create_task(count(5))

    # Методы для работы с каждой конкретной задачей
    print(f'Результат метода done() - {short_task_22.done()}')
    print(f'Результат метода cancelled() - {short_task_22.cancelled()}')
    print(f'Результат метода cancel() - {short_task_22.cancel("Принудительно остановил")}')

    # Метод .wait() для нескольких задач
    done, pending = await asyncio.wait((
        short_task_11, short_task_12,
        short_task_21, short_task_22,
        long_task_one, long_task_two)
    )
    print('\n', done, '\n', sep='')

    # Проверка состояний после работы метода .wait()
    print(f'Повторный результат метода done() - {short_task_22.done()}')
    print(f'Повторный результат метода cancelled() - {short_task_22.cancelled()}')

    # Метод .result() возвращает исключение CancelledError,
    # если ранее к объекту применялся метод .cancel()
    try:
        short_task_22.result()
    except asyncio.CancelledError:
        print('Исключение CancelledError')


if __name__ == "__main__":
    # event_loop
    asyncio.run(main())
