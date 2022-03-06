import time


def func():
    for n in range(10):
        print(1)
        time.sleep(1)
        print(2)


def main():
    star_time = time.time()
    func()
    finish_time = time.time()
    release_time = finish_time - star_time
    print(release_time)


if __name__ == '__main__':
    main()
