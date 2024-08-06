import math, random
from constants import *

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        self.board = [[0 for i in range(self.row_length)] for i in range(self.row_length)]

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            for i in row:
                print(i, end=" ")
            print("")
        return

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        for i in self.board[row]:
            if i == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for i in self.board:
            if i[col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + self.box_length):
            for j in range(col_start, col_start + self.box_length):
                if self.board[i][j] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num):
            return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(digits)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start + i][col_start + j] = digits.pop()

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        total_removed = 0
        while total_removed < self.removed_cells:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                total_removed += 1


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Cell:
    def __init(self, value, row, col, screen, selected=False): #Emily
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = selected
        self.sketched_value = None
        self.cell_size = 50
        self.font = pygame.font.Font(None, 36)


    def set_cell_value(self, value): #Emily
        self.value = value

    def set_sketched_value(self, value): #Emily
        self.sketched_value = value

    def draw(self): #Emliy
        backgound = (255, 255, 255)

        if self.selected:
            outline = (255, 0, 0)
        else:
            outline = (0, 0, 0)

        pygame.draw.rect(self.screen, backgound, pygame.Rect(self.col * cell_size, self.row * cell_size, cell_size, cell_size))
        pygame.draw.rect(self.screen, outline, pygame.Rect(self.col * cell_size, self.row * cell_size, cell_size, cell_size), 2)

        if self.value != 0:
            text_surface = self.font.render(str(self.value), True, (0, 0, 0))  # Black text color
            text_rect = text_surface.get_rect(
                center=(self.col * self.cell_size + self.cell_size // 2, self.row * self.cell_size + self.cell_size // 2))
            self.screen.blit(text_surface, text_rect)

import pygame
class Board: #rohan
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.size = 9
        pass

    def draw(self): #rohan
        for i in range(10):
            thickness = bold_line_thickness if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, self.height), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * cell_size), (self.width, i * cell_size), thickness)

    def select(self, row, col): #rohan
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, row, col): #rohan
        x, y = pygame.mouse.get_pos()
        cell_size = 60
        row = y // cell_size
        col = x // cell_size

        if 0 <= row < 9 and 0 <= col < 9:
            return row, col
        return None

    def clear(self): #rohan
        if self.selected_cell and self.selected_cell.selected:
            self.selected_cell.value = None

    def sketch(self, value): #rohan
        if self.selected_cell and self.selected_cell.selected:
            self.selected_cell.sketch = value

    def place_number(self):
        if self.selected_cell: #Emily
            row, col = self.selected_cell
            self.cells[row][col].set_cell_value(value)

    def reset_to_original(self): #Rohan/repeating function
        self.cells = [[Cell(row, col) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.font = pygame.font.SysFont(None, 40)
        pass

    def reset_to_original(self): #Emily
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].set_cell_value(0)

    def is_full(self): #Emily
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

    pass

