# Извлечь числа из строк и прибавить к ним число 10

operation1 = "результат операции: 42"
operation2 = "результат операции: 514"
result_of_work = "результат работы программы: 9"

# Находим индекс чисел внутри строки
index1 = operation1.rfind(" ")
index2 = operation2.rfind(" ")
index3 = result_of_work.rfind(" ")

# Находим числа с помошью индекса, преобразовываем их в Int и прибавляем к ним 10
print(int(operation1[index1:]) + 10)
print(int(operation2[index2:]) + 10)
print(int(result_of_work[index3:]) + 10)
