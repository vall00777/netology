def get_cookbook(file):
     book = open('cookbook.txt').read().split('\n\n')
     cook_book = {}
     for dish in book:
          dish = dish.split('\n')
          cook_book[dish[0]] = []
          for ingredients in dish[2:]:
               ingredients = ingredients.split(' | ')
               if not ingredients[0]: break
               cook_book[dish[0]].append({'ingridient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]})
               return cook_book
def get_shop_list_by_dishes(dishes, person_count):
     out = {}
     for dish in dishes:
          try:
               for dish in cook_book[dish]:
                    out[dish['ingridient_name']] = {}
                    out[dish['ingridient_name']]['measure'] = dish['measure']
                    out[dish['ingridient_name']]['quantity'] = dish['quantity'] *2
          except KeyError:
               print('Блюда не существует')
          return(out)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

