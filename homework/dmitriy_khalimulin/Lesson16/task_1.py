import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

# Подключение к базе данных
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)

cursor = db.cursor()

# Путь к файлу для чтения
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_file_path_csv = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Чтение данных из файла CSV
with open(eugene_file_path_csv, newline='') as csv_file:
    file_data = csv.reader(csv_file)

    # Пропускаем заголовок
    next(file_data)

    missing_data = []

    for row in file_data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

        query = '''
        SELECT COUNT(*) FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON s.id = b.taken_by_student_id 
        LEFT JOIN marks m ON s.id = m.student_id 
        LEFT JOIN lessons l ON m.lesson_id = l.id 
        LEFT JOIN subjets s2 ON l.subject_id = s2.id 
        WHERE s.name = %s AND s.second_name = %s 
        AND g.title = %s AND b.title = %s 
        AND s2.title = %s AND l.title = %s 
        AND m.value = %s
        '''

        cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
        result = cursor.fetchone()

        # Если записи нет, добавляем строку в список отсутствующих данных
        if result[0] == 0:
            missing_data.append(row)

    # Выводим отсутствующие данные
    if missing_data:
        print("Данных не хватает для следующих записей:")
        for missing_row in missing_data:
            print(missing_row)
    else:
        print("Все данные из CSV файла найдены в базе данных.")

db.close()
