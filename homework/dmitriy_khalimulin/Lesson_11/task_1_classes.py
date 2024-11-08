# Создаем родительский класс
class Book:
    material = "paper"
    text = True

    def __init__(self, book_name, author, number_of_pages, isbn, reservation):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reservation = reservation

    # Создаем метод print_details в родительском классе Book, который печатает детали о книге.
    def print_details(self):
        print(f"Название: {self.book_name}, "
              f"Автор: {self.author}, "
              f"Количество страниц: {self.number_of_pages}, "
              f"Материал: {self.material}", end="")
        if self.reservation:
            print(", Зарезервирована")
        else:
            print("")


# Создаем переменную для каждой книги родительского класса и присваиваем им данные #
book_1 = Book(
    "Overlord", "LobanovDA",
    315, "984-5-0500-0765-7", False
)
book_2 = Book(
    "Start", "KonovalovAM",
    234, "324-5-0394-4423-7", True
)
book_3 = Book(
    "Close the door", "PivinRD",
    341, "344-5-2234-5673-7", False
)
book_4 = Book(
    "Open the door", "KuraevIF",
    531, "336-5-6934-2572-7", False
)
book_5 = Book(
    "Slow a car", "PapaevJF",
    544, "877-5-6574-3578-7", False
)


# Создаем дочерний класс
class SchoolTextbooks(Book):

    def __init__(self, book_name, author, number_of_pages, isbn, reservation, item, clas, tasks):
        super().__init__(book_name, author, number_of_pages, isbn, reservation)
        self.item = item
        self.clas = clas
        self.tasks = tasks

    # Создаем метод print_details1 в дочернем классе SchoolTextbooks, который печатает детали об учебнике.
    def print_details1(self):
        print(f"Название: {self.book_name}, "
              f"Автор: {self.author}, "
              f"Количество страниц: {self.number_of_pages}, "
              f"Предмет: {self.item}, "
              f"Класс: {self.clas}", end="")
        if self.reservation:
            print(", Зарезервирована")
        else:
            print("")


# Создаем переменную для каждого учебника дочернего класса и присваиваем им данные #
textbook_1 = SchoolTextbooks(
    "Алгебра", "Иванов", 200, "984-5-0500-0765-7", True,
    "Математика", 9, "Задачи по алгебре"
)
textbook_2 = SchoolTextbooks(
    "Геометрия", "Петров", 554, "454-5-5567-2214-7", False,
    "Черчение", 8, "Задачи по геометрии"
)
textbook_3 = SchoolTextbooks(
    "Физика", "Петров", 635, "223-5-3345-5525-7", False,
    "Аэродинамика", 10, "Задачи по физике"
)


# Распечатываем функцию print_details для каждой книги родительского класса
book_1.print_details()
book_2.print_details()
book_3.print_details()
book_4.print_details()
book_5.print_details()

# Распечатываем функцию print_details1 для каждого учебника дочернего класса
textbook_1.print_details1()
textbook_2.print_details1()
textbook_3.print_details1()
