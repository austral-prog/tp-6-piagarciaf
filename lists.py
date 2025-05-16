def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements[:]
    if len(lista) >5:
        del lista[5]
    if len(lista) >4:
        del lista[4]
    if len(lista) >0:
        del lista[0]
    return lista

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements
print(add_elements(['Red', 'Green', 'White', 'Black']))

def is_empty(list_to_check):
        return len(list_to_check) ==0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >=3 and len(list_to_compare2) >=3:
        return list_to_compare1[2] == list_to_compare2[2]
    else: 
        return False

def list_of_lists(list_of_lists_to_modify):
    a = list_of_lists_to_modify[0][:2]
    b = list_of_lists_to_modify[1][1:4]
    c = list_of_lists_to_modify[2][-2:]
    return [a, b, c]
