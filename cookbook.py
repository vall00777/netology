def get_cookbook(file):
     book = open('cookbook.txt').read().split('\n\n')
     cook_book = {}
     for i in book:
          i = i.split('\n')
          cook_book[i[0]] = []
          for j in i[2:]:
               j = j.split(' | ')
               if not j[0]: break
               cook_book[i[0]].append({'ingridient_name': j[0], 'quantity': int(j[1]), 'measure': j[2]})
               return cook_book


def get_shop_list_by_dishes(dishes, person_count):
     out = {}
     for i in dishes:
          try:
               for i in cook_book[i]:
                    
                    out[i['ingridient_name']] = {}
                    out[i['ingridient_name']]['measure'] = i['measure']
                    out[i['ingridient_name']]['quantity'] = i['quantity'] *2
          except KeyError:
               print('Блюда не существует')

     return(out)

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
