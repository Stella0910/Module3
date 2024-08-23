def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [20, 'String', [1, 2, 3]]
values_dict = {'a': 30, 'b': 'String2', 'c': [4, 5, 6]}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [10.15, 'word']


print_params(*values_list_2, 42)

