from decimal import Decimal
from datetime import datetime

def add(items, title, amount, expiration_date=None):
    if isinstance(expiration_date, str): # если пришла строка, превращаем её в дату
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()

    new_good = {
        'amount': Decimal(str(amount)),
        'expiration_date': expiration_date
    }

    if title not in items:
        items[title] = [] # если продукта нет в списке, он создается
    items[title].append(new_good) # добавляем продукт


def add_by_note(items, note):
    parts = note.split()

    if '-' in parts[-1]: # проверяем наличие срока годности у товара
        expiration_date = datetime.strptime(parts[-1], '%Y-%m-%d').date()
        parts.pop(-1)
    else:
        expiration_date = None

    amount = parts.pop(-1) # записываем количество, не переводим его в Decimal, т.к. это сделает ф-я add
    title = ' '.join(parts) # склеиваем название
    add(items, title, amount, expiration_date)

def find(items, needle):
    result = []
    for title in items: # прохожу по всем названиям продуктов (по ключам в словаре)
        if needle.lower() in title.lower():
            result.append(title)
    return result

def amount(items, needle):
    found_products = find(items, needle) # находим нужные продукты
    total = Decimal('0')
    for title in found_products: # проверяем количество в каждой партии нужного продукта
        for x in items[title]:
            total += x['amount']
    return total


goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта "Пельмени Универсальные"
        {'amount': Decimal('0.5'), 'expiration_date':
         datetime(2023, 7, 15).date()},
        # Вторая партия
        {'amount': Decimal('2'), 'expiration_date':
         datetime(2023, 8, 1).date()},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ]
}

# добавляем продукты через заметку
add_by_note(goods, 'Яйца куриные 10 2023-09-30')
add_by_note(goods, 'Молоко 2.5')

# ищем продукты
print("Поиск 'яйца':", find(goods, 'яйца'))
print("Поиск 'молоко':", find(goods, 'молоко'))

# считаем общее количество
print("Всего яиц:", amount(goods, 'яйца'))
print("Всего молока:", amount(goods, 'молоко'))
print("Всего пельменей:", amount(goods, 'пельмени'))


# тест для ф-ии add()
test_items = {}

# проверяем добавление с датой (строкой)
add(test_items, 'Яблоки', 2, '2023-10-25')
# проверяем добавление без даты
add(test_items, 'Хлеб', 1)
# проверяем добавление второй партии того же продукта
add(test_items, 'Яблоки', 1.5, '2023-10-26')

print(test_items)