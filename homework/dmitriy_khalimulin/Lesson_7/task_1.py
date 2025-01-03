# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
number = 534

while True:
    try:
        user_input = int(input('Угадайте цифру: '))
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")
        continue
    if user_input == number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')

print('До свидания')
