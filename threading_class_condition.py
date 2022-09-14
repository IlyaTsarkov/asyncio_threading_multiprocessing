import random
import threading
import string
import time


class GiftsSend:
    """В классе имитируем отправку подарков для победителей,
    но создаем условие, что имя победителя должно быть написано
    с заглавной буквы"""

    def __init__(self, count_winners):
        # Передаем число победителей
        self.count_winners = count_winners
        # Создаем экземпляр Condition()
        self.condition = threading.Condition()
        # Забираем в переменную все заглавные буквы
        self.upper_alphabets = string.ascii_uppercase

    def who_win(self, winner_name):
        print(f'Проверяем {winner_name} на соответствие')
        # with заменяет .acquire() и .release()

        with self.condition:
            # Проверяем, что первая буква большая
            if winner_name[0] in self.upper_alphabets:
                print(f'{winner_name} получает подарок')
            # Если первая буква маленькая ставим на ожидание
            else:
                # Через 5 секунд выводим ожидание разблокируется
                # и мы увидим имена, которые не получили подарок
                self.condition.wait()
                print(f'{winner_name} Без подарка')


if __name__ == '__main__':
    # Генерируем 10 победителей со случайными именами
    # И запускаем для каждого .who_win()
    send_example = GiftsSend(10)
    alphabets = string.ascii_letters
    upper_alphabets = string.ascii_uppercase

    for winner in range(send_example.count_winners):
        name = ''.join(random.choice(alphabets) for i in range(random.randint(2, 5)))
        send_thread = threading.Thread(target=send_example.who_win, args=[name], name=name)
        send_thread.start()

        time.sleep(1)
        # Проверяем каждое имя, если первая буква маленькая - снимаем .wait()
        if send_thread.name[0] not in upper_alphabets:
            with send_example.condition:
                send_example.condition.notify()
