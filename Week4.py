def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

tic = "WES.AX"
print(tic)
qan_tic()


def mk_csv_name(tic):                   # (1)
    tic = tic.lower()                   # (2)
    tic_base = tic.split('.')[0]        # (3)
    return f'{tic_base}_stk_prc.csv'    # (4)

name = mk_csv_name('QAN.AX')            # (5)
print(name)                             # (6)

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
def give_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


even_numbers = give_even(A)
print(even_numbers)

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
squared_list = [x ** 2 for x in lst if x ** 2 >150]
print(squared_list)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
unique_integer = list(set([x for x in numbers if x % 2 == 0]))
print(unique_integer)


