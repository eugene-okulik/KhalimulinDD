# Добавление модуля Decimal, для уменьшения чисел, так как стотысячное число не отображается.
from decimal import Decimal


def fibonacci_generator():
    a, b = Decimal(0), Decimal(1)
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

fifth_number = next(fib_gen)
for _ in range(4):  # Пропускаем первые 4 числа
    fifth_number = next(fib_gen)

two_hundredth_number = next(fib_gen)
for _ in range(194):  # Пропускаем еще 194 числа (уже пропустили 5)
    two_hundredth_number = next(fib_gen)

thousandth_number = next(fib_gen)
for _ in range(800):  # Пропускаем еще 800 чисел
    thousandth_number = next(fib_gen)

hundred_thousandth_number = next(fib_gen)
for _ in range(99000):  # Пропускаем еще 99000 чисел
    hundred_thousandth_number = next(fib_gen)


print("Пятое число:", fifth_number)
print("Двухсотое число:", two_hundredth_number)
print("Тысячное число:", thousandth_number)
print("Стотысячное число:", hundred_thousandth_number)
