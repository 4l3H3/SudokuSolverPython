import time

matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

found_solutions = 0

EMPTY = 0

start_time = time.time()


def fits_in_column(number, xindex, matrix):
    for yindex in range(0, len(matrix)):
        if matrix[xindex][yindex] == number:
            return False
    return True


def fits_in_row(number, yindex, matrix):
    for xindex in range(0, len(matrix)):
        if matrix[xindex][yindex] == number:
            return False
    return True


def fits_in_square(number, xindex, yindex, matrix):
    for x_index in range(xindex - xindex % 3, xindex - xindex % 3 + 3):
        for y_index in range(yindex - yindex % 3, yindex - yindex % 3 + 3):
            if matrix[x_index][y_index] == number:
                return False
    return True


def fits_in_tile(number, xindex, yindex, matrix):
    return fits_in_column(number, xindex, matrix) and fits_in_row(number, yindex, matrix) and fits_in_square(number,
                                                                                                             xindex,
                                                                                                             yindex,
                                                                                                             matrix)


def print_solution(matrix):
    global found_solutions
    global start_time
    end_time = time.time() - start_time
    found_solutions += 1
    print("Loesung " + str(found_solutions) + " gefunden nach " + str(end_time))
    for xindex in range(len(matrix)):
        print(str(matrix[xindex][:]) + " ")
    print()


def solve_sudoku(matrix):
    for xIndex in range(len(matrix)):
        for yindex in range(len(matrix[xIndex])):
            if matrix[xIndex][yindex] == EMPTY:
                for number in range(1, 10):
                    if fits_in_tile(number, xIndex, yindex, matrix):
                        matrix[xIndex][yindex] = number
                        if solve_sudoku(matrix):
                            print_solution(matrix)
                        matrix[xIndex][yindex] = 0
                return False
    return True


solve_sudoku(matrix)
