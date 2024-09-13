# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
from datetime import datetime

incorrect_date = "Jan 15, 2023 - 12:05:33"

correct_date = datetime.strptime(incorrect_date, '%b %d, %Y - %H:%M:%S')

print(correct_date.strftime("%B"))
print(correct_date.strftime("%d.%m.%Y, %H:%M"))
