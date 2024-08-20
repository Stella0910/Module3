calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    result_string = (len(string), string.upper(), string.lower())
    count_calls()
    print(result_string)


def is_contains(string, lst):
    string = string.lower()
    lst = ' '.join(lst).lower()
    lst = lst.split()
    count_calls()
    if string in lst:
        return True
    else:
        return False


string_info('Capybara')
string_info('Armageddon')
string_info('Не армагедон, все ок :)')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Строчка', ['сТрока', 'сТрОЧкА', 'строченькА']))
print(calls)
