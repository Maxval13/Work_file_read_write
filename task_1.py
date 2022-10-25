# Задача 1
cook_book = {}

from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    for l in file:
        dish_name = l.strip()
        dep = {"name": dish_name, "ingredients": []}
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            dep["ingredients"].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        cook_book = cook_book | {dep["name"]: dep["ingredients"]}

pprint(cook_book, sort_dicts=False)

# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    list_dish = {}
    for i in dishes:
        if i in cook_book.keys():
            for l in cook_book[i]:
                person_quantity = int(l["quantity"]) * person_count
                list_dish.update({l["ingredient_name"]: {"measure": l["measure"], "quantity": person_quantity}})
    return list_dish


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задача 3
import os

outfile = 'output.txt'
text_l = {}

for file in os.listdir("sorted"):
    with open(os.path.join("sorted", file), encoding='utf8') as f:
        content = f.readlines()
        content_ = ''.join(content)
        len1 = len(content)
        text_l[file] = {len1: content_}

res = []

with open('output.txt', 'w', encoding='UTF-8') as of:
    for k, v in text_l.items():
        for k1, v1 in v.items():
            res.append([k1, k, v1])
    res1 = sorted(res)
    for i in range(len(res1)):
        of.writelines([f'{res1[i][1]}\n{res1[i][0]}\n{res1[i][2]}\n'])