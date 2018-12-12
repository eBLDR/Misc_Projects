#! /usr/bin/python3

"""
- THIS CODE IS DESIGN TO RUN IN THE TERMINAL -

Conway's Game of Life
 0 - dead cell
 1 - alive cell
-1 - border of the board

RULES:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    - Wikipedia
"""

import random
import time
import os


class Universe:
    """ Environment object, where the cells 'live'. """
    
    def __init__(self, rows, cols, chance_alive, max_generations):
        self.cells_alive = 0
        self.generation = range(1, max_generations + 1)
        self.chance_alive = chance_alive  # initial factor of a cell being alive
        self.environment = self.initial_generation(rows, cols)
    
    @staticmethod
    def initial_status(factor):
        """ Decides if a cell is alive in the first generation. """
        
        n = random.randint(1, 100)
        if n <= factor:
            return True
    
    def initial_generation(self, rows, cols):
        """ Creates the initial array. """
        
        array = []
        for i in range(rows):
            array_row = []
            for j in range(cols):
                if j == 0 or i == 0 or (i == rows - 1) or (j == cols - 1):  # borders
                    array_row.append(-1)
                else:
                    status = self.initial_status(self.chance_alive)  # initial cell, alive or dead?
                    if status:
                        array_row.append(1)
                        self.cells_alive += 1
                    else:
                        array_row.append(0)
            array.append(array_row)
        
        return array


def display_grid(univ, gen):
    """ Displays the grid:
    # - border
    . - alive cell
      - dead cell """
    
    os.system("clear")
    
    print("Game of Life by eBLDR! -- Generation: {:4} -- Cells alive: {:3}".format(gen, univ.cells_alive))
    
    array = univ.environment
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == -1:
                print("#", end=' ')
            elif array[i][j] == 1:
                print(".", end=' ')
            else:
                print(" ", end=' ')
        print()


def process_next_gen(univ):
    """ Creates the array for the following generation. """
    
    current = univ.environment
    next_gen = []
    
    univ.cells_alive = 0  # restarting the counter
    
    for i in range(len(current)):
        next_row = []
        for j in range(len(current[i])):
            if current[i][j] == -1:  # borders
                next_row.append(current[i][j])
            else:
                cell_status = assess_neighbours(i, j, current)
                next_row.append(cell_status)
                if cell_status == 1:
                    univ.cells_alive += 1
        next_gen.append(next_row)
    
    univ.environment = next_gen


def assess_neighbours(x, y, current):
    """ Assesses the future of the cell depending on surrounding neighbours. """
    
    neighbour_cells = 0
    for i in range(x - 1, x + 2):  # to assess only the surrounding 3x3 grid
        for j in range(y - 1, y + 2):
            # excluding itself and borders
            if not (i == x and j == y) and current[i][j] != -1:
                neighbour_cells += current[i][j]  # will add 1 if there is a cell, 0 otherwise
    
    # RULE 1, death due to underpopulation
    if current[x][y] == 1 and neighbour_cells < 2:
        return 0
    # RULE 3, death due to overpopulation
    elif current[x][y] == 1 and neighbour_cells > 3:
        return 0
    # RULE 4, alive by reproduction
    elif current[x][y] == 0 and neighbour_cells == 3:
        return 1
    # RULE 2, remains alive if it was alive and neighbour cells is 2 or 3,
    # and remains death if it was death and neighbour cells are not 3
    else:
        return current[x][y]


def get_data(min_, max_, prompt):
    """ Collects needed input from keyboard. """
    while True:
        data = input(prompt)
        if data.isdigit():
            data = int(data)
            if min_ <= data <= max_:
                return data
            else:
                print("Minimum: {}, Maximum: {}".format(min_, max_))
        else:
            print("Must be positive integer.")


def main():
    """ Main loop, collects data for the initial conditions and runs the program. """
    
    # input some variables
    init_factor = get_data(1, 100, "Chances of being alive in the first generation expressed in %: ")
    max_gen = get_data(1, 10000, "Number of generations to display: ")
    
    # creating the universe object, including first generation of cells
    universe = Universe(ROWS, COLUMNS, init_factor, max_gen)
    
    for gen in universe.generation:
        # displaying current distribution
        display_grid(universe, gen)
        
        # calculating next distribution
        process_next_gen(universe)
        
        # adding some delay
        time.sleep(DELAY)
        
        # manual forwarding -- DISABLED --
        # input("Press <return> to display next generation.")


# CONSTANTS
# size of the board (linux default terminal's size is 24x80)
ROWS = 22
COLUMNS = 33
# delay between generations in seconds
DELAY = 0.15

if __name__ == '__main__':
    # loop, why not
    Play = True
    while Play:
        main()
        # round finished
        input("Finished! Press <return>.")
        while True:
            more_or_no = input("'More' for another round. 'Quit' to quit.\n").lower()
            if more_or_no == 'quit':
                Play = False
                break
            elif more_or_no == 'more':
                break
            else:
                print("What?")
