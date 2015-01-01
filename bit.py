
WIDTH = 50
HEIGHT = 50

class Bit:
    instances = []

    def __init__(self, x, y):
        Bit.instances.append(self)
        self.x = x
        self.y = y

    def check_adjacent(self, grid):
        results = {}
        for x, y in [(self.x + i, self.y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
                if (0 <= x < HEIGHT) and (0 <= y <= WIDTH):
                    if y == WIDTH:
                        y = 0
                    if x == HEIGHT:
                        x = 0
                    results[x,y] = grid[x][y]
        return results

    def growth(self, grid):
        adjacent_cells = self.check_adjacent(grid)
        growth_value = [k for k,v in adjacent_cells.items() if v == 1]
        if grid[self.x][self.y] == 1:
            if growth_value < 2:
                grid[self.x][self.y] = 0
            elif growth_value > 3:
                grid[self.x][self.y] = 0
        else:
            if growth_value == 3:
                grid[self.x][self.y] = 1
        