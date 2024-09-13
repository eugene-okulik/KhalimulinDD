# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
import random

while True:
    try:
        salary = int(input("Введите вашу зарплату: "))
    except ValueError:
        print("Необходимо ввести число")
        continue
    bonus = random.choice([True, False])  # Случайным образом выбираем True или False

    if bonus:
        bonus_amount = random.randint(1, 3000)  # Генерируем случайный бонус от 1 до 5000
        salary += bonus_amount
        print(f"{bonus_amount}, {bonus}, ${salary}")
    else:
        print(f"0, {bonus}, ${salary}")
