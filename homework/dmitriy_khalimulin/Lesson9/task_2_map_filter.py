# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
temperatures = (
    [
        20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
        22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
    ]
)

# Создание списка с помощью функции "filter"
hot_days_filter = list(filter(lambda x: x > 28, temperatures))


# Создание списка с помощью функции "map"
def is_hot(temp):
    return temp if temp > 28 else None


hot_days_map = list(filter(None, map(is_hot, temperatures)))


print(hot_days_filter)  # Распечатать список температут для функции "filter"
print(max(hot_days_filter))  # Распечатать максимальную температуру из списка
print(min(hot_days_filter))  # Распечатать минимальную температуру из списка

print(hot_days_map)  # Распечатать список температут для функции "map"
print(
    round(sum(hot_days_map) / len(hot_days_map))
)  # Распечатать среднюю температуру списка с округлением
