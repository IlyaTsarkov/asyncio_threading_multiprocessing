import multiprocessing.managers
import random


def get_rand_number():
    return random.randint(1, 100)


multiprocessing.managers.BaseManager.register('get_r_n', callable=get_rand_number)
manager = multiprocessing.managers.BaseManager(address=('', 8080), authkey=b'123')
server = manager.get_server()
print(server.address)
server.serve_forever()
