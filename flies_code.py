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
import os
current = os.getcwd()
folder_name = ".\sorted"
file_list = []

for file in os.listdir(folder_name):
        if file.endswith('.txt'):
            with open(os.path.join(folder_name, file), 'rt', encoding='utf-8') as f:
                read = f.read().strip()
                count_string = int(read.count('\n') + 1)
                file_list.append([str(count_string), file, read])
sorted_list = sorted(file_list)
with open(os.path.join("result.txt"), "wt", encoding='utf-8') as f:
        for file in sorted_list:
            result = f"имя: {file[1]}\nкол-во строк: {file[0]}\n{file[2].strip()}\n\n"
            f.write(result)
