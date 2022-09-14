import asyncio
import aiohttp


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

    @staticmethod
    def json_render(obj):
        """
        Создаем экземпляр класса.
        Данные для переменных забираем из словаря
        полученных с запросом данных
        """
        return Album(obj['userId'], obj['id'], obj['title'])


def show_albums(albums):
    """Выводим заголовки полученных альбомов"""
    for album in albums:
        print(f'{album.album_title}')


async def main():
    """Создаем aiohttp.ClientSession(), от него мы можем асинхронно совершать запросы к 100 разным серверам"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/albums?userId=1') as resp:
            albums_json = await resp.json()
            albums = [Album.json_render(album) for album in albums_json]
            show_albums(albums)


if __name__ == '__main__':
    asyncio.run(main())
