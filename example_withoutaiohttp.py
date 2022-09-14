import requests


class Album:
    """
    Класс для объявления альбомов.
    Источник https://jsonplaceholder.typicode.com/albums
    Каждый альбом содержит 3 параметра.
    """
    def __init__(self, user_id, album_id, album_title):
        self.user_id = user_id
        self.album_id = album_id
        self.album_title = album_title

    @classmethod
    def json_render(cls, obj):
        """
        Создаем экземпляр класса.
        Данные для переменных забираем из словаря
        полученных с запросом данных
        """
        user_id = obj['userId']
        album_id = obj['id']
        album_title = obj['title']
        return Album(user_id, album_id, album_title)


def albums_by_user(user):
    """
    Функция для запроса к альбомам, забирает альбомы переданного пользователя.
    Полученные сырые данные преобразуем к списку словарей
    и из каждого словаря создаем экземпляр класса Album методом json_render()
    """
    url = f'https://jsonplaceholder.typicode.com/albums?userId={user}'

    response = requests.get(url)
    albums_json = response.json()

    return [Album.json_render(album) for album in albums_json]


def show_albums(albums):
    """Выводим заголовки полученных альбомов"""
    for album in albums:
        print(f'{album.album_title}')


def main():
    """Запускаем сбор альбомов пользователя с id=1"""
    n = 1
    while n <= 10:
        albums = albums_by_user(n)
        show_albums(albums)
        n += 1


if __name__ == '__main__':
    main()
