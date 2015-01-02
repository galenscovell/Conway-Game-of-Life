
from bit import Bit
import pygame
import argparse

# Color setup
BACKGROUND = ( 44,  62,  80)
WORLD      = ( 52,  73,  94)
CRITTER    = (242, 202,  39)
DEATH      = (155,  89, 182)

# Window settings
pygame.init()
CELLSIZE = 9
MARGIN = 1
HEIGHT = 50
WIDTH = 50
screen_size = [500, 500]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Cellular Automata | Conway's Game of Life")


class World:

    def placeCritter(self, grid):
        pos = pygame.mouse.get_pos()
        column = pos[0] // (CELLSIZE + MARGIN)
        row = pos[1] // (CELLSIZE + MARGIN)
        grid[row][column] = 1

    def updateWorld(self, grid):
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):
                if grid[y][x] == 1:
                    color = CRITTER
                else:
                    color = WORLD
                pygame.draw.rect(screen, color, 
                    [(MARGIN + CELLSIZE) * x + MARGIN, 
                    (MARGIN + CELLSIZE) * y + MARGIN, 
                    CELLSIZE, CELLSIZE])

    def createWorld(self):
        grid = []
        for y in range(0, HEIGHT):
            grid.append([])
            for x in range(0, WIDTH):
                bit = Bit(x, y)
                grid[y].append(0)
        return grid


def main(args):

    world = World()
    clock = pygame.time.Clock()

    running = True
    sim_start = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                world.placeCritter(new_world)
                world.updateWorld(new_world)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sim_start = True
                elif event.key == pygame.K_SPACE:
                    sim_start = False
                    screen.fill(BACKGROUND)
                    new_world = world.createWorld()
                    world.updateWorld(new_world)
                    ticks = args.num_ticks

        if sim_start and ticks > 0:
            for bit in Bit.instances:
                bit.growth_calculate(new_world)
            for bit in Bit.instances:
                bit.growth(new_world)
            world.updateWorld(new_world)
            ticks -= 1

        pygame.display.flip()
        clock.tick(args.framerate)

    pygame.quit()
    quit()

def parse_arguments():
    parser = argparse.ArgumentParser(description = "Conway's Game of Life: Cellular Automata")
    parser.add_argument('-t', '--num_ticks', help = "Runtime length. (Default: 1000)", default = 1000, type = int)
    parser.add_argument('-fps', '--framerate', help = "Framerate (Default: 10)", default = 10, type = int)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main(parse_arguments())