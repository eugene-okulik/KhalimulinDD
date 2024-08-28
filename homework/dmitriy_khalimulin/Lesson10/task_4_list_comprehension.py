# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь

PRICE_LIST = '''Ретрадь 50р
                Книга 200р
                Ручка 100р
                Карандаш 70р
                Альбом 120р
                Пенал 300р
                Рюкзак 500р'''

price_dict = {}

for line in PRICE_LIST.splitlines():
    name, price = line.split()
    price_dict[name] = int(price[:-1])  # Удаляем "р" с цены

print(price_dict)
