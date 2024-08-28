# Напишите программу:
# Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).

# Создайте декоратор, который декорирует функцию calc и
# управляет тем какая операция будет произведена:
#
# - если числа равны, то функция calc вызывается с операцией сложения этих чисел
# - если первое больше второго, то происходит вычитание второго из певрого
# - если второе больше первого - деление первого на второе
# - если одно из чисел отрицательное - умножение
def arithmetic_decorator(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        else:
            operation = 'Неизвестная операция'
        return func(first, second, operation)
    return wrapper


@arithmetic_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return "Неизвестная операция"


while True:
    try:
        first_number = int(input("Введите первое число: "))
        second_number = int(input("Введите второе число: "))
        result = calc(first_number, second_number)
        print(f"Результат: {result}")
        break
    except ValueError:
        print("Некорректный ввод. Введите целые числа.")