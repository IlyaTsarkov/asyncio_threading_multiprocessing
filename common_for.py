import time


def func(arg_1_1):
    for i in range(arg_1_1):
        yield i
        time.sleep(1)


def run(arg_1_2):
    for i in func(arg_1_2 + 1):
        print(i)
        print('asyncio.sleep(1)')


def main():
    star_time = time.time()
    run(2)
    run(4)
    finish_time = time.time()
    release_time = finish_time - star_time
    print(release_time)


if __name__ == '__main__':
    main()


