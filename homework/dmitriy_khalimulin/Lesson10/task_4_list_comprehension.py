# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь

PRICE_LIST = '''Ретрадь 50р
                Книга 200р
                Ручка 100р
                Карандаш 70р
                Альбом 120р
                Пенал 300р
                Рюкзак 500р'''

price_dict = dict(
    line.split() for line in PRICE_LIST.splitlines()
)  # Используем dict comprehension

price_dict = {
    name: int(price[:-1]) for name, price in price_dict.items()
}  # Используем dict comprehension для преобразования цен

print(price_dict)
