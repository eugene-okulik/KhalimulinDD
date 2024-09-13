import os
import datetime

# Путь к файлу для чтения
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_file_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')

# Путь для создания нового файла
new_file_path = os.path.dirname(__file__)
new_file = os.path.join(new_file_path, 'data_2.txt')


# Открываем исходный файл для чтения и создаем новый файл для записи
with open(eugene_file_path, 'r') as file, open(new_file, 'w') as output_file:
    for line in file:
        # Разделяем строку на номер, дату и действие
        parts = line.split(' - ')
        if len(parts) < 2:
            continue  # Пропускаем строки без корректной структуры

        # Номер и дата
        number, date_str = parts[0].split('. ')
        date_str = date_str.strip()
        action = parts[1].strip()

        # Преобразуем строку с датой в объект datetime
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        # Выполняем действия в зависимости от номера
        if number == '1':
            # Добавляем неделю к дате
            new_date = date + datetime.timedelta(weeks=1)
            result = f"Дата через неделю: {new_date}\n"
            print(result.strip())
            output_file.write(result)

        elif number == '2':
            # Определяем день недели
            day_of_week = date.strftime('%A')  # Название дня недели
            result = f"День недели для даты {date}: {day_of_week}\n"
            print(result.strip())
            output_file.write(result)

        elif number == '3':
            # Считаем, сколько дней прошло с этой даты до текущей
            current_date = datetime.datetime.now()
            days_diff = (current_date - date).days
            result = f"Количество дней с даты {date}: {days_diff} дней назад\n"
            print(result.strip())
            output_file.write(result)
