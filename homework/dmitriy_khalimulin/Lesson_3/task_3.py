# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
from math import sqrt

number1 = 24525
number2 = 37645

# Среднее арифметическое
avg_arithmetic = (number1 + number2) / 2
print("Среднее арифметическое:", avg_arithmetic)

# Среднее геометрическое
avg_geometric = sqrt(number1 * number2)
print("Среднее геометрическое:", avg_geometric)
