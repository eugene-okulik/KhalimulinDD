import mysql.connector as mysql

# Подключение к базе данных
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Создание курсора
cursor = db.cursor()

# # Создание студента
student_create = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(student_create, ('Denis', 'Kurganov'))
student_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM students WHERE id = {student_id}")
student_data = cursor.fetchone()
print(f"Создание студента:\n{student_data}\n")


# Создание книг для студента
books_create = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    books_create, [
        ('Cat and Dog', student_id),
        ('Orange and Banana', student_id),
        ('Pen and Pencil', student_id)
    ]
)
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
books_data = cursor.fetchall()
print(f"Создание книг для студента:\n{books_data}\n")


# Создание группы
groups_create = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(groups_create, ('Super group', 'aug 2024', 'sep 2024'))
groups_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM `groups` WHERE id = {groups_id}")
groups_data = cursor.fetchone()
print(f"Создание группы:\n{groups_data}\n")


# Определение студента в группу
cursor.execute('UPDATE students SET group_id = %s WHERE id = %s', (groups_id, student_id))
cursor.execute(f"SELECT * FROM students WHERE group_id = {groups_id}")
student_in_group_data = cursor.fetchone()
print(f"Определение студента в группу:\n{student_in_group_data}\n")


# Создание предметов
subjets_create = "INSERT INTO subjets (title) VALUES (%s)"
titles = ['Super class', 'Super function', 'Super metod']

subject_ids = []

for title in titles:
    cursor.execute(subjets_create, (title,))
    last_id = cursor.lastrowid
    subject_ids.append(last_id)

select_query = f"SELECT * FROM subjets WHERE id IN ({','.join(['%s'] * len(subject_ids))})"
cursor.execute(select_query, tuple(subject_ids))
subjets_data = cursor.fetchall()
print(f"Создание предметов:\n{subjets_data}\n")


# Создание занятий
lessons_create = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

lessons_ids = []

cursor.executemany(
    lessons_create, [
        ('Lesson_1', subject_ids[0]),
        ('Lesson_2', subject_ids[0]),
        ('Lesson_3', subject_ids[1]),
        ('Lesson_4', subject_ids[1]),
        ('Lesson_5', subject_ids[2]),
        ('Lesson_6', subject_ids[2]),
    ]
)

select_lessons = f"SELECT * FROM lessons WHERE subject_id IN ({','.join(['%s'] * len(subject_ids))})"
cursor.execute(select_lessons, tuple(subject_ids))
lessons_data = cursor.fetchall()
for lesson in lessons_data:
    lessons_ids.append(lesson[0])
print(f"Создание занятий:\n{lessons_data}\n")


# Проставить оценки
marks_create = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"

cursor.executemany(
    marks_create, [
        ('Great', lessons_ids[0], student_id),
        ('Good', lessons_ids[0], student_id),
        ('Badly', lessons_ids[1], student_id),
        ('Fine', lessons_ids[1], student_id),
        ('Average', lessons_ids[2], student_id),
        ('Not good', lessons_ids[2], student_id),
    ]
)

select_marks = f"SELECT * FROM marks WHERE lesson_id IN ({','.join(['%s'] * len(lessons_ids))})"
cursor.execute(select_marks, tuple(lessons_ids))
marks_data = cursor.fetchall()
print(f"Проставить оценки:\n{marks_data}\n")


# Получить все оценки студента
select_all_marks = '''
SELECT s.*, m.value as ratings
FROM students s
JOIN marks m ON s.id = m.student_id
WHERE s.id = %s
'''
cursor.execute(select_all_marks, (student_id,))
marks_all_data = cursor.fetchall()
print(f"Получить все оценки студента:\n{marks_all_data}\n")


# Получить все книги студента
select_all_books = '''
SELECT s.*, b.title as books
FROM students s
JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = %s
'''
cursor.execute(select_all_books, (student_id,))
books_all_data = cursor.fetchall()
print(f"Получить все книги студента:\n{books_all_data}\n")


# Получить всю информацию о студенте
all_information_student = '''
SELECT s.*, g.title as `group`, b.title as books, m.value as ratings, l.title as lesson, s2.title as subgets
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = %s
'''
cursor.execute(all_information_student, (student_id,))
all_information_student_data = cursor.fetchall()
print(f"Получить всю информацию о студенте:\n{all_information_student_data}\n")

db.commit()
db.close()
