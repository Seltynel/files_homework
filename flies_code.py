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

pprint(cook_book, sort_dicts=False)
