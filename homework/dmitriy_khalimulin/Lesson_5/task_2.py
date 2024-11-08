# Извлечь числа из строк и прибавить к ним число 10

operation1 = "результат операции: 42"
operation2 = "результат операции: 514"
result_of_work = "результат работы программы: 9"

# Находим индекс чисел внутри строки
index1 = operation1.index(":")
index2 = operation2.index(":")
index3 = result_of_work.index(":")

index1 = int(operation1[index1:].strip(":"))
index2 = int(operation2[index2:].strip(":"))
index3 = int(result_of_work[index3:].strip(":"))

# Находим числа с помошью индекса, преобразовываем их в Int и прибавляем к ним 10
print(index1 + 10)
print(index2 + 10)
print(index3 + 10)
