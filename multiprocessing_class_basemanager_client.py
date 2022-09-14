import multiprocessing.managers

multiprocessing.managers.BaseManager.register('get_r_n')
manager = multiprocessing.managers.BaseManager(address=('localhost', 8080), authkey=b'123')
manager.connect()

result = manager.get_r_n()
print(result)
