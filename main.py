import numpy as np

# sudoku backtrack solve: https://www.youtube.com/watch?v=G_UYXzGuqvM

sudoku = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]])


def solvable(x, y):
    global sudoku
    for i in [n for n in range(9) if n != x]:
        if sudoku[y][i] == sudoku[y][x]:
            return False
    for i in [n for n in range(9) if n != y]:
        if sudoku[i][x] == sudoku[y][x]:
            return False
    for i in range(9):
        x_corner = int(x / 3) * 3
        y_corner = int(y / 3) * 3
        x_new = x_corner + ((x_corner + i) % 3)
        y_new = y_corner + int((i / 3))
        if x_new == x or y_new == y:
            continue
        if sudoku[y_new][x_new] == sudoku[y][x]:
            return False
    return True


def solve():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    sudoku[y][x] = n
                    if solvable(x, y):
                        solve()
                    sudoku[y][x] = 0
                return
    print(sudoku, "\n")


if __name__ == '__main__':
    solve()

