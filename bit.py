
WIDTH = 50
HEIGHT = 50

class Bit:
    """Cellular automaton unit."""
    instances = []

    def __init__(self, x, y):
        Bit.instances.append(self)
        self.x = x
        self.y = y
        self.growth_value = 0

    def check_adjacent(self, grid):
        """
        Create dictionary of all adjacent cells contents, adjusting 
            for horizontal and vertical wrap-around.
        Dictionary contents are either 0 (empty) or 1 (full).
        """
        results = 0
        for x, y in [(self.x + i, self.y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
                if y >= WIDTH:
                    y = 0
                elif y < 0:
                    y = WIDTH - 1
                if x >= HEIGHT:
                    x = 0
                elif x < 0:
                    x = WIDTH - 1
                if grid[x][y] == 1:
                    results += 1
        return results

    def growth_calculate(self, grid):
        """Growth value is the amount of adjacent filled spaces."""
        self.growth_value = self.check_adjacent(grid)

    def growth(self, grid):
        """
        Cellular events based on bit growth value.
        If cell is currently filled:
            Value larger than 3 or less than 2 causes cell to die.
            Value of exactly 3 causes cell to persist.
        If cell is currently empty:
            Value of exactly 3 causes cell to become alive.
        """
        if grid[self.x][self.y] == 1:
            if self.growth_value < 2:
                grid[self.x][self.y] = 0
            elif self.growth_value > 3:
                 grid[self.x][self.y] = 0
            else:
                pass
        elif grid[self.x][self.y] == 0:
            if self.growth_value == 3:
                 grid[self.x][self.y] = 1
            else:
                pass
        