-- Создание студента
INSERT INTO students (name, second_name) VALUES ('Dmitriy', 'Khalimulin');


-- Создание книг для студента
INSERT INTO books (title, taken_by_student_id) VALUES ('SRE', 2117),
													  ('QA Engineer', 2117),
													  ('Frontend', 2117),
													  ('Backend', 2117);


-- Создание группы
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Python book', 'Aug 2024', 'Okt 2024');


-- Определение студета в группу
UPDATE students SET group_id = 1923 WHERE id = 2117;


-- Создание учебных предметов
INSERT INTO subjets (title) VALUES ('Class'), ('Function'), ('Metod');


-- Создание занятий
INSERT INTO lessons (title, subject_id) VALUES ('Lesson Class', 2718),
											   ('Lesson Class homework', 2718),
											   ('Lesson Function', 2719),
											   ('Lesson Function homework', 2719),
											   ('Lesson Metod', 2720),
											   ('Lesson Metod homework', 2720);


-- Проставка оценок
INSERT INTO marks (value, lesson_id, student_id) VALUES ('Great', 5659, 2117),
														('Good', 5660, 2117),
														('Badly', 5661, 2117),
														('Fine', 5662, 2117),
														('Average', 5663, 2117),
														('Not good', 5664, 2117);


-- Получить все оценки студента
SELECT s.*, m.value as ratings FROM students s
JOIN marks m ON s.id = m.student_id
WHERE s.id = 2117;


-- Получить все книги студента
SELECT s.*, b.title as books FROM students s
JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = 2117;


-- Получить всю информацию о студенте
SELECT s.*, g.title as `group`,
       b.title as books, m.value as ratings,
       l.title as lesson, s2.title as subgets
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = 2117;