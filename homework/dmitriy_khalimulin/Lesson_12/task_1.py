class Flower:
    """Общий класс для цветов."""
    def __init__(self, name, color, price, stem_length, freshness_days):
        self.name = name
        self.color = color
        self.price = price
        self.stem_length = stem_length
        self.freshness_days = freshness_days

    def __str__(self):
        return (f"{self.name} ({self.color}), "
                f"цена: {self.price}, "
                f"длина стебля: {self.stem_length}, "
                f"свежесть: {self.freshness_days} дней")


class Rose(Flower):
    """Класс для роз."""
    def __init__(self, name, color, price, stem_length, freshness_days, thorns=True):
        super().__init__(name, color, price, stem_length, freshness_days)
        self.thorns = thorns


class Tulip(Flower):
    """Класс для тюльпанов."""
    def __init__(self, name, color, price, stem_length, freshness_days, shape="classic"):
        super().__init__(name, color, price, stem_length, freshness_days)
        self.shape = shape


class Bouquet:
    """Класс для букета."""
    def __init__(self):
        self.flowers = []
        self.cost = 0

    def add_flower(self, f):
        """Добавляет цветок в букет."""
        self.flowers.append(f)
        self.cost += f.price

    def get_cost(self):
        """Возвращает стоимость букета."""
        return self.cost

    def get_withering_time(self):
        total_freshness = sum(flwr.freshness_days for flwr in self.flowers)
        return total_freshness / len(self.flowers)

    def sort_by(self, key, reverse=False):
        self.flowers.sort(key=lambda fl: getattr(fl, key), reverse=reverse)

    def search_by_freshness(self, min_freshness, max_freshness):
        return [flwr for flwr in self.flowers
                if min_freshness <= flwr.freshness_days <= max_freshness]


# Создание цветов
rose1 = Rose("Красная роза", "красный", 50, 60, 7, thorns=True)
rose2 = Rose("Белая роза", "белый", 45, 55, 6, thorns=True)
tulip1 = Tulip("Тюльпан", "желтый", 30, 40, 5, shape="classic")
tulip2 = Tulip("Тюльпан", "красный", 35, 45, 4, shape="parrot")

# Создание букета
my_bouquet = Bouquet()
my_bouquet.add_flower(rose1)
my_bouquet.add_flower(rose2)
my_bouquet.add_flower(tulip1)
my_bouquet.add_flower(tulip2)

# Вывод информации о букете
print("Цветы в букете:")
for flower in my_bouquet.flowers:
    print(flower)

print(f"Стоимость букета: {my_bouquet.get_cost()} рублей")
print(f"Среднее время увядания: {my_bouquet.get_withering_time()} дней")

# Сортировка и поиск
print("\nСортировка по свежести:")
my_bouquet.sort_by('freshness_days')
for flower in my_bouquet.flowers:
    print(flower)

print("\nПоиск цветов со свежестью от 4 до 6 дней:")
fresh_flowers = my_bouquet.search_by_freshness(4, 6)
for flower in fresh_flowers:
    print(flower)
