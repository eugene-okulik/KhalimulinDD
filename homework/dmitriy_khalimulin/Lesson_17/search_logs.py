import os
import argparse


def find_text_in_files(file, search_text):
    # Проходим по всем файлам в указанной папке
    for eugene_logs, _, files in os.walk(file):
        for file_name in files:
            file_path = os.path.join(eugene_logs, file_name)
            # Открываем файл и читаем его построчно
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    if search_text in line:
                        # Разбиваем строку на слова
                        words = line.split()

                        # Находим индекс слова, содержащего искомый текст
                        for i, word in enumerate(words):
                            if search_text in word:
                                # Получаем 5 слов до и после найденного слова
                                start = max(0, i - 5)
                                end = min(len(words), i + 6)

                                # Формируем кусок строки
                                context = ' '.join(words[start:end])

                                # Выводим результат
                                print(f"Файл: {file_name}, строка: {line_number}")
                                print(f"Контекст: {context}\n")


# Парсинг аргументов командной строки
def main():
    parser = argparse.ArgumentParser(description='Поиск текста в логах')
    parser.add_argument('file', help='Путь к папке с логами')
    parser.add_argument('--text', help='Текст для поиска')
    parser.add_argument('--full', help='Текст для поиска', action='store_true')
    args = parser.parse_args()

    # Запуск поиска
    find_text_in_files(args.file, args.text)


if __name__ == '__main__':
    main()
