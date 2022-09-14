import multiprocessing
import string


class Compound:
    """Класс для хранения списка пользователей"""

    def __init__(self, main_p_name):
        self.name = main_p_name

    @staticmethod
    def get_result(result):
        """Метод для демонстрации Pool().map()"""
        current_p = multiprocessing.current_process().name
        print(f'Данные - {result}'
              f'\nТекущий процесс - {current_p}')

        return result


if __name__ == '__main__':
    # Все буквы, из них сгенерируем случайный список
    alphabets = string.ascii_letters
    # Служебная информация
    ex_p = Compound(multiprocessing.current_process().name)
    print(f'Главный процесс - {ex_p.name}')
    # Запуск процессов через Pool()
    with multiprocessing.Pool(processes=4) as p:
        # Генерация списка букв разбитых по одной
        r_list = [rand_info for rand_info in alphabets]
        # .map() для объединенного запуска всех процессов
        ex_p = p.starmap(ex_p.get_result, r_list[:3])
        # В случае асинхронных аналогов процессы нужно закрывать и джоинить
        print(ex_p.next())
        print(ex_p.next())
        print(ex_p.next())
