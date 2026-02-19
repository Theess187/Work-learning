
while True:
    x = input('Введите что-нибудь: ')
    for i in 'Hello world':
        if i == x:
            print('такая буква есть')
            break
    else:
        print('такой буквы нет')