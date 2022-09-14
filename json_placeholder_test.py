import requests


class Album:
    def __init__(self, user_id, album_id, album_title):
        self.user_id = user_id
        self.album_id = album_id
        self.album_title = album_title

    @classmethod
    def json_render(cls, obj):
        user_id = obj['userId']
        album_id = obj['id']
        album_title = obj['title']
        return Album(user_id, album_id, album_title)


def albums_by_user(user):
    url = f'https://jsonplaceholder.typicode.com/albums?userId={user}'

    response = requests.get(url)
    albums_json = response.json()

    return [Album.json_render(album) for album in albums_json]


print([album.album_title for album in albums_by_user(1)])

