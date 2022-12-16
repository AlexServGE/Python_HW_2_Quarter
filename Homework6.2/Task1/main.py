def print_operation_table(operation, num_rows=9, num_columns=9):
    for el_1 in range(1, num_rows + 1):
        for el_2 in range(1, num_columns + 1):
            print('{0:10d}'.format(operation(el_1,el_2)), end='')
        print()


print_operation_table(lambda x, y: x * y)
