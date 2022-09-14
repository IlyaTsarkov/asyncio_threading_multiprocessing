import multiprocessing


class Compound:
    """Класс для хранения списка пользователей"""

    def __init__(self, info):
        self.info = info

    def example_send_info(self, pipe):
        """Через канал для передачи данных помещаем в pipe переданную строку"""
        pipe.send(self.info)
        pipe.close()


if __name__ == '__main__':
    ex_compound = Compound('some info')
    # Экземпляр Pipe() содержит канал для передачи данных и для получения
    o_p, i_p = multiprocessing.Pipe()
    # В экземпляр в качестве аргумента отдаем канала input()
    for pr in range(2):
        multiprocessing.Process(target=ex_compound.example_send_info, args=(i_p,)).start()
        # Получаем данные из Pipe() через канал output()
        print(o_p.recv())
        print(o_p.fileno())
        print(i_p.fileno())
        print(o_p.poll())
