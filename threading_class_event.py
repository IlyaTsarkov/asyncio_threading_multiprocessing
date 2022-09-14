import threading
import time

# Создаем экземпляр Event()
event = threading.Event()


def gifts_prepare():
    # Изначальное состояние экземпляра Event() False,
    # пока состояние False все, что ниже .wait() не начнется
    event.wait(timeout=3)
    print(f"\nПодарок для {threading.current_thread().name} отправлен")


if __name__ == '__main__':
    # Главный поток, в котором имитируется работа
    print(f'Отправка подарков 5 пользователям')

    # Цикл для создания и запуска 5 потоков
    for user in range(5):
        threading.Thread(target=gifts_prepare, name=f'Пользователь {user}').start()
        print(f'\nПодарок для пользователя {user} готов')
        time.sleep(1)

    # Только когда существует 5 активных потоков флаг экземпляра Event() становится True
    # И инструкция после .wait() могут быть выполнены
    if threading.active_count() >= 5:
        event.set()
