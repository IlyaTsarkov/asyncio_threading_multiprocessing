import threading


def gift_prepare():
    print(f'Поздравляем! Для вас подарок!\n'
          f'Он будет готов через 30 секунд...\n')


def gift_ready():
    email = input(f'Подарок готов, для его получения введите ваш email\n'
                  f'email - ')

    if email:
        print('Спасибо! Подарок уже у вас на почте')
    else:
        print('Извините, время вышло...')


if __name__ == '__main__':
    gift_prepare()

    send_gift_thread = threading.Timer(interval=5, function=gift_ready)
    send_gift_thread.start()

