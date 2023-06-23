# Задание 1
from pprint import pprint

with open('recipes.txt', 'rt', encoding= 'UTF-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients

# pprint(cook_book, sort_dicts=False)

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    for element in dishes:
        if element in cook_book:
            for dish in cook_book[element]:
                persons = int(dish['quantity']) * person_count
                result = {
                    dish['ingredient_name']: {'measure': dish['measure'], 'quantity': persons}
                }
                print(result)
        else:
            print('Нет такого блюда')
            return
    
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задание 3
with open('./sorted/1.txt', 'rt', encoding= 'UTF-8') as file_first, open('./sorted/2.txt', 'rt', encoding= 'UTF-8') as file_second, open('./sorted/3.txt', 'rt', encoding= 'UTF-8') as file_third, open('./sorted/result.txt', 'wt', encoding= 'UTF-8') as file_res:
    count_first = 0
    name_first = '1.txt'
    count_second = 0
    name_second = '2.txt'
    count_third = 0
    name_third = '3.txt'
    for line1 in file_first:
        line1.strip()
        # file_res.write(line1)
        count_first += 1
    for line2 in file_second:
        line2.strip()
        # file_res.write(line2)
        count_second  += 1
    for line3 in file_third:
        line3.strip()
        # file_res.write(line3)
        count_third += 1
    print(sorted([count_first, count_second, count_third]))

# Готово. На всякий случай скину часть результата:
# Строка 1 файла 2.txt - Тревога началась в тринадцать часов ноль две минуты.
# Строка 1 файла 1.txt - Начальник полиции
# Строка 2 файла 1.txt - лично позвонил в шестнадцатый участок. А спустя одну минуту тридцать секунд