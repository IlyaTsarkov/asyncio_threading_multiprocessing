import threading
import time
import random
import datetime


class GiftsSend:
    """В классе имитируем отправку подарков для победителей,
    но создаем условие, что сначала мы собираем нужное количество подарков
    для всех победителей и только после этого отправляем их"""

    def __init__(self, count_winners):
        # Передаем число победителей
        self.count_winners = count_winners

        # Создаем экземпляр класса Barrier()
        self.barrier = threading.Barrier(self.count_winners)

    def gift_send(self, winner):
        """Установим разное время на сбор подарка для каждого победителя
        Таким образом пока все подарки собраны не будут их отправка не случится"""
        print(f'Собираем подарок для {winner}')
        # Имитируем разное время на подготовку каждого подарка
        time.sleep(random.randint(2, 6))
        print(f'Подарок для {winner} собран в {datetime.datetime.now()}')
        # Пока все потоки не упрутся в .wait() выполнение функции не продолжится
        print(self.barrier.parties)
        self.barrier.wait()

        print(f'\nОтправляем подарок для {winner}, в {datetime.datetime.now()}')


if __name__ == '__main__':
    # Экземпляр с количеством победителей
    FirstSend = GiftsSend(3)

    # Создаем поток для каждого победителя и запускаем
    for winner in range(FirstSend.count_winners):
        send_thread = threading.Thread(target=FirstSend.gift_send, args=str(winner)).start()
