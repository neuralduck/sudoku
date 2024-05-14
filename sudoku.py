import sys
sys.setrecursionlimit(1500)
class Sudoku:
    def __init__(self):
        self.grid = [
        [0, 0, 4, 0, 5, 0, 0, 0, 0],
        [9, 0, 0, 7, 3, 4, 6, 0, 0],
        [0, 0, 3, 0, 2, 1, 0, 4, 9],
        [0, 3, 5, 0, 9, 0, 4, 8, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 0],
        [0, 7, 6, 0, 1, 0, 9, 2, 0],
        [3, 1, 0, 9, 7, 0, 2, 0, 0],
        [0, 0, 9, 1, 8, 2, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 1, 0, 0],
        ]
        self.N = 9
    def __str__(self):
        final = ''
        for n, row in enumerate(self.grid):
            final += f'{row[0]} {row[1]} {row[2]} | {row[3]} {row[4]} {row[5]} | {row[6]} {row[7]} {row[8]} \n'
            if n == 2 or n == 5:

                final += f"{'-'*21}\n"
        return final
    def check(self, row, column, num):
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        for i in range(9):
            if self.grid[i][column] == num:
                return False
        center = [(row//3)*3+1, ((column//3)*3+1)]
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if self.grid[center[0]+i][center[1]+j] == num:
                    return False
        return True

    def solve(self, row, column):
        if (row == self.N-1) and (column == self.N):
            return True

        if column == self.N:
            row += 1
            column = 0

        if self.grid[row][column] > 0:
            return self.solve(row, column + 1)
        for num in range(1, self.N+1):
            if self.check(row, column, num):
                self.grid[row][column] = num

                if self.solve(row, column + 1):
                    return True
            self.grid[row][column] = 0
        return False
s = Sudoku()
print(s)
s.solve(0, 0)
print('Solution: ')
print(s)