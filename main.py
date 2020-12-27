import numpy as np


# sudoku backtrack solve: https://www.youtube.com/watch?v=G_UYXzGuqvM
def solvable(x, y, matrix):
    for i in [n for n in range(9) if n != x]:
        if matrix[y][i] == matrix[y][x]:
            return False
    for i in [n for n in range(9) if n != y]:
        if matrix[i][x] == matrix[y][x]:
            return False
    for i in range(9):
        x_corner = int(x / 3) * 3
        y_corner = int(y / 3) * 3
        x_new = x_corner + ((x_corner + i) % 3)
        y_new = y_corner + int((i / 3))
        if x_new == x or y_new == y:
            continue
        if matrix[y_new][x_new] == matrix[y][x]:
            return False
    return True


def solve(matrix):
    for y in range(9):
        for x in range(9):
            if matrix[y][x] != 0:
                continue
            for n in range(1, 10):
                matrix[y][x] = n
                if solvable(x, y, matrix):
                    solve(matrix)
                matrix[y][x] = 0
            return
    print(matrix, "\n")


if __name__ == '__main__':
    sudoku_template = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]])

    solve(np.array([
        [0, 0, 0, 0, 0, 2, 0, 0, 3],
        [0, 8, 0, 0, 4, 0, 5, 0, 0],
        [3, 0, 2, 5, 0, 0, 0, 7, 0],
        [0, 0, 7, 0, 0, 4, 0, 0, 0],
        [5, 0, 0, 0, 9, 6, 3, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 2, 1, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 2, 5]])
    )
    solve(np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 3, 0, 7, 5, 0, 0],
        [3, 1, 0, 0, 8, 0, 7, 6, 4],
        [0, 3, 6, 0, 0, 0, 0, 0, 1],
        [0, 5, 0, 0, 0, 9, 4, 0, 3],
        [8, 7, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 7, 1, 3, 0, 0, 0],
        [5, 0, 0, 2, 0, 0, 0, 0, 0]])
    )
