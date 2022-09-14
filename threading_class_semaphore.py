import threading
import time


class GiftsSend:
    """В классе имитируем отправку подарков для победителей,
    но создаем условие, что одновременно можно формировать только 2 подарка,
    и только после того как они сформируются можно начинать формировать следующие"""

    def __init__(self):
        # Создаем экземпляр класса Semaphore()
        self.moment_count = threading.BoundedSemaphore(value=2)

    def gift_send(self, winner):
        # Приводим поток в работу, тем самым занимаем слот в Semaphore()
        print(f'\nОповещаем победителя {winner}')
        self.moment_count.acquire()

        # Имитируем затрату времени на работу
        print(f'\nФормируем подарок для {winner}')
        time.sleep(2)
        print('\nМеста на отправку заняты')

        # Отправляем подарок, тем самым освобождая слот в Semaphore()
        print(f'\nОтправляем подарок для {winner}')
        try:
            self.moment_count.release(2)
        except ValueError:
            print(f'Количество realise больше value')

    def gift_winners(self, count):
        """Формируем количество потоков по числу переданных победителей"""
        for winner in range(count):
            send_thread = threading.Thread(target=self.gift_send, args=[winner]).start()


if __name__ == '__main__':
    FirstSend = GiftsSend()
    FirstSend.gift_winners(4)
