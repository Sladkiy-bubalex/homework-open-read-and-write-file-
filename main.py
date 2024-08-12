  # Выполнение 1 задачи
cook_book = {}

with open('cookbook.txt', encoding='utf-8') as file:
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break
        ingredient_count = int(file.readline().strip())
        ingredients = []

        for _ in range(ingredient_count):
            ingredient_line = file.readline().strip()
            ingredient_name, quantity, measure = ingredient_line.split(' | ')

            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            }
            ingredients.append(ingredient)

        cook_book[dish_name] = ingredients
        file.readline()

  # Выполнение 2 задачи
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      for ing in cook_book[dish]:
        if ing['ingredient_name'] in shop_list:
          shop_list[ing['ingredient_name']]['quantity'] += ing['quantity'] * person_count
        else:
          shop_list[ing['ingredient_name']] = {
            'measure': ing['measure'],
            'quantity': ing['quantity'] * person_count
          }
    else:
      print(f'Блюда {dish} нет в книге рецептов')
  return shop_list

  # Выполнение 3 задачи
all_file_count = {}
for name_file in ['1.txt', '2.txt', '3.txt']:
    with open(name_file, encoding='utf-8') as file:
        file_count = sum(1 for line in file)
        all_file_count[name_file] = file_count
sorted_files = sorted(all_file_count.items(), key=lambda item: item[1])

with open('final text', 'w', encoding='utf-8') as fin_t:
    for name_file, count in sorted_files:
        with open(name_file, encoding='utf-8') as file:
            fin_t.write(f'{name_file}\n')
            fin_t.write(f'{all_file_count[name_file]}\n')
            fin_t.write(file.read())
            fin_t.write('\n')

