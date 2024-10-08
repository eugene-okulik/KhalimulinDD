# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished"
# после выполнения декорированной функции.
def finish_me(func):        # Создаем функцию "finish_me" с аргументом "func"

    def wrapper():          # Создаем функцию "wrapper" внутри функции "finish_me"
        func()              # Выполняем функцию "example"
        print('finished')   # Выполняем распечатку текста "finished"

    return wrapper          # Выводим из функции значение функции "wrapper"


@finish_me                  # Запускаем декоратор "finish_me"
def example():              # Создаем функцию "example" без аргументов
    print("print me")       # Выполняем распечатку текста "print me"


example()                   # Запускаем функцию "example"
