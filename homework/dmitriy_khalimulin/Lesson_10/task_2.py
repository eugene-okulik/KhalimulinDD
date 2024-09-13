# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция

# Обьяснение
# 1. def repeat_me(count=1): repeat_me принимает аргумент count (по умолчанию 1).
# 2. def decorator(func)::  Внутри repeat_me  определяется функция decorator,
#    которая принимает функцию func (которая будет декорироваться).
# 3. def wrapper(text)::  wrapper принимает только аргумент текст
# 4. return decorator:  repeat_me  возвращает  decorator
def repeat_me(count=1):
    def decorator(func):
        def wrapper(text):
            for _ in range(count):
                func(text)
        return wrapper
    return decorator

# - @repeat_me(count=2)  вызов декоратора с аргументом count=2.
# - repeat_me  создаёт и возвращает  decorator, который обертывает example.
# - decorator  создаёт и возвращает  wrapper, которая теперь использует значение count,
#   переданное через repeat_me.


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
