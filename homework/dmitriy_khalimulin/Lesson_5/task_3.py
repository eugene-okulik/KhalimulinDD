# Распечатайте текст, который будет использовать данные из этих списков.

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

string1 = ', '.join(students)
string2 = ', '.join(subjects)

text = f'Student {string1} study these subjects: {string2}'
print(text)
