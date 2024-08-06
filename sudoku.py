#main function for the game
import sys
import pygame
from constants import *
from sudoku_generator import *

def draw_game_start(screen):
    screen.fill(BG_COLOR)

    #Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 40)

    #Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH//2, HEIGHT//2 -150))
    screen.blit(title_surface, title_rectangle)

    #Initialize buttons
    #Initialize text first
    easy_text = button_font.render("Easy", 0, WHITE)
    med_text = button_font.render("Medium", 0, WHITE)
    hard_text = button_font.render("Hard", 0, WHITE)

    quit_text = button_font.render("Quit", 0, WHITE)

    #Initialize button Background color and text
    #Easy button
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    #Medium button
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(LINE_COLOR)
    med_surface.blit(med_text, (10, 10))

    #Hard button
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    #Quit button
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    #Initialize button rectangles
    easy_rectangle = easy_surface.get_rect(center=(WIDTH//2 - 150, HEIGHT//2 + 50))
    med_rectangle = med_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH//2 + 150, HEIGHT//2 + 50))
    quit_rectangle = quit_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 150))

    #Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #Select difficulty from buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                elif med_rectangle.collidepoint(event.pos):
                    return "medium"
                elif hard_rectangle.collidepoint(event.pos):
                    return "hard"
                elif quit_rectangle.collidepoint(event.pos):
                    sys.exit()

        pygame.display.update()

def draw_board():
    #Draw horizontal lines
    for i in range(1, SIZE):
        if i % 3 == 0:
            LINE_WIDTH = 5
            pygame.draw.line(screen, LINE_COLOR, (0, i * BOX_SIZE), (WIDTH, i * BOX_SIZE), LINE_WIDTH)
        else:
            LINE_WIDTH = 2
            pygame.draw.line(screen, LINE_COLOR, (0, i*BOX_SIZE), (WIDTH, i*BOX_SIZE), LINE_WIDTH)

    #Draw vertical lines
    for i in range(1, SIZE):
        if i % 3 == 0:
            LINE_WIDTH = 5
            pygame.draw.line(screen, LINE_COLOR, (i * BOX_SIZE, 0), (i * BOX_SIZE, HEIGHT), LINE_WIDTH)
        else:
            LINE_WIDTH = 2
            pygame.draw.line(screen, LINE_COLOR, (i*BOX_SIZE, 0), (i*BOX_SIZE, HEIGHT), LINE_WIDTH)

def draw_numbers():
    #Draws the numbers for the base of the level
    number_font = pygame.font.Font(None, NUMBER_FONT)
    num1_surf = number_font.render("1", 0, NUMBER_COLOR)
    num2_surf = number_font.render("2", 0, NUMBER_COLOR)
    num3_surf = number_font.render("3", 0, NUMBER_COLOR)
    num4_surf = number_font.render("4", 0, NUMBER_COLOR)
    num5_surf = number_font.render("5", 0, NUMBER_COLOR)
    num6_surf = number_font.render("6", 0, NUMBER_COLOR)
    num7_surf = number_font.render("7", 0, NUMBER_COLOR)
    num8_surf = number_font.render("8", 0, NUMBER_COLOR)
    num9_surf = number_font.render("9", 0, NUMBER_COLOR)

    #Renders the numbers
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 1:
                num1_rect = num1_surf.get_rect(center=(col*BOX_SIZE + BOX_SIZE/2, row*BOX_SIZE + BOX_SIZE/2))
                screen.blit(num1_surf, num1_rect)
            elif board[row][col] == 2:
                num2_rect = num2_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num2_surf, num2_rect)
            elif board[row][col] == 3:
                num3_rect = num3_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num3_surf, num3_rect)
            elif board[row][col] == 4:
                num4_rect = num4_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num4_surf, num4_rect)
            elif board[row][col] == 5:
                num5_rect = num5_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num5_surf, num5_rect)
            elif board[row][col] == 6:
                num6_rect = num6_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num6_surf, num6_rect)
            elif board[row][col] == 7:
                num7_rect = num7_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num7_surf, num7_rect)
            elif board[row][col] == 8:
                num8_rect = num8_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num8_surf, num8_rect)
            elif board[row][col] == 9:
                num9_rect = num9_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
                screen.blit(num9_surf, num9_rect)

def select_box(col, row):
    #Function to highlight the user-selected box. Box will remain highlighted and may be selected again.
    select_surface = pygame.Surface(size=(WIDTH//SIZE - 2, HEIGHT//SIZE - 2))
    select_surface.fill(SELECT_COLOR)
    screen.blit(select_surface, (col*BOX_SIZE + 3, row*BOX_SIZE + 3))
    pygame.display.update()


def fill_box(num, row, col):
    #Fills the box with a number - this has an error where a box can be filled with multiple numbers. I'm assuming this
    # has to do with an error allowing a box to be selected multiple times.
    number_font = pygame.font.Font(None, NUMBER_FONT)
    add_num1_surf = number_font.render("1", 0, USER_NUMBER_COLOR)
    add_num2_surf = number_font.render("2", 0, USER_NUMBER_COLOR)
    add_num3_surf = number_font.render("3", 0, USER_NUMBER_COLOR)
    add_num4_surf = number_font.render("4", 0, USER_NUMBER_COLOR)
    add_num5_surf = number_font.render("5", 0, USER_NUMBER_COLOR)
    add_num6_surf = number_font.render("6", 0, USER_NUMBER_COLOR)
    add_num7_surf = number_font.render("7", 0, USER_NUMBER_COLOR)
    add_num8_surf = number_font.render("8", 0, USER_NUMBER_COLOR)
    add_num9_surf = number_font.render("9", 0, USER_NUMBER_COLOR)

    if num == 1:
        add_num1_rect = add_num1_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num1_surf, add_num1_rect)
    elif num == 2:
        add_num2_rect = add_num2_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num2_surf, add_num2_rect)
    elif num == 3:
        add_num3_rect = add_num3_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num3_surf, add_num3_rect)
    elif num == 4:
        add_num4_rect = add_num4_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num4_surf, add_num4_rect)
    elif num == 5:
        add_num5_rect = add_num5_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num5_surf, add_num5_rect)
    elif num == 6:
        add_num6_rect = add_num6_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num6_surf, add_num6_rect)
    elif num == 7:
        add_num7_rect = add_num7_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num7_surf, add_num7_rect)
    elif num == 8:
        add_num8_rect = add_num8_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num8_surf, add_num8_rect)
    elif num == 9:
        add_num9_rect = add_num9_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE / 2, row * BOX_SIZE + BOX_SIZE / 2))
        screen.blit(add_num9_surf, add_num9_rect)

    if board[row][col] == 0:
        board[row][col] = num
    else:
        return

    pygame.display.update()

def validate(board):
    sets = []
    for i in range(len(board)):
        for j in range(len(board)):
            num = board[i][j]
            if num != "0":
                sets += [(i, num), (num, j), (i // 3, j // 3, num)]

    for i in sets:
        if sets.count(i) > 1:
            return False
        else:
            return True

def draw_game_over(screen, correct):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if correct:
        text = "Level Completed"
    else:
        text = "Level Failed"

    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    menu_surf = game_over_font.render("Press M to return to the main menu...", 0, LINE_COLOR)
    menu_rect = menu_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 150))
    screen.blit(menu_surf, menu_rect)

    pygame.display.update()

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    game_over = False
    completed = False
    correct = True

    difficulty = draw_game_start(screen)
    if difficulty == "easy":
        board = generate_sudoku(9, 30)
    elif difficulty == "medium":
        board = generate_sudoku(9, 40)
    elif difficulty == "hard":
        board = generate_sudoku(9, 50)

    screen.fill(BG_COLOR)
    draw_board()
    draw_numbers()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not completed:
                x, y = event.pos
                row = int(y // BOX_SIZE)
                col = int(x // BOX_SIZE)
                if board[row][col] == 0:
                    select_box(col, row)
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_1]:
                    fill_box(1, row, col)
                elif pygame.key.get_pressed()[pygame.K_2]:
                    fill_box(2, row, col)
                elif pygame.key.get_pressed()[pygame.K_3]:
                    fill_box(3, row, col)
                elif pygame.key.get_pressed()[pygame.K_4]:
                    fill_box(4, row, col)
                elif pygame.key.get_pressed()[pygame.K_5]:
                    fill_box(5, row, col)
                elif pygame.key.get_pressed()[pygame.K_6]:
                    fill_box(6, row, col)
                elif pygame.key.get_pressed()[pygame.K_7]:
                    fill_box(7, row, col)
                elif pygame.key.get_pressed()[pygame.K_8]:
                    fill_box(8, row, col)
                elif pygame.key.get_pressed()[pygame.K_9]:
                    fill_box(9, row, col)

                if 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 0 not in board[3] and 0 not in board[4] and 0 not in board[5] and 0 not in board[6] and 0 not in board[7] and 0 not in board[8]:
                    completed = True
                    correct = validate(board)
                    draw_game_over(screen, correct)
                    pygame.display.update()

                    if event.type == pygame.KEYDOWN:
                        if pygame.key.get_pressed()[pygame.K_m]:
                            correct = True
                            completed = False

                            difficulty = draw_game_start(screen)
                            if difficulty == "easy":
                                board = generate_sudoku(9, 2)
                            elif difficulty == "medium":
                                board = generate_sudoku(9, 40)
                            elif difficulty == "hard":
                                board = generate_sudoku(9, 50)

                            screen.fill(BG_COLOR)
                            draw_board()
                            draw_numbers()




        pygame.display.update()
