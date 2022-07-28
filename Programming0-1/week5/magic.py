def magic_square(square):
    main_diagonal_sum = 0
    second_diagonal_sum = 0
    length = len(square)

    for i in range(length):
        main_diagonal_sum += square[i][i]
        second_diagonal_sum += square[i][length - 1 - i]

    if main_diagonal_sum != second_diagonal_sum:
        return False

    for index_row in range(0, length):
        row_sum = 0
        for index_col in range(length):
            row_sum += square[index_row][index_col]
        if row_sum != main_diagonal_sum:
            return False
    for index_col in range(length):
        col_sum = 0
        for index_row in range(length):
            col_sum += square[index_row][index_col]
        if col_sum != main_diagonal_sum:
            return False

    return True


square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
square2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
square3 = [ [1, 1, 1], [1, 1, 1], [1, 1, 1] ]

print(magic_square(square1))
print(magic_square(square2))
print(magic_square(square3))
