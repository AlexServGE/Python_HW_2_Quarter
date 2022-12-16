def same_by(function, some_list):
    return not [1 for el in some_list if not function(el)]


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')
