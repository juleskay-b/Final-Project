#main function for the game (please let me know if i messed up)
import sys
import pygame
from constants import *
from sudoku_generator import *

# constants I added for sketch function (ana's changes)
SKETCH_FONT = 20
SKETCH_COLOR = (100, 100, 100)

# global variables for selected cell & sketched numbers (ana's changes)
selected_row, selected_col = None, None
sketched_numbers = {}

def draw_game_start(screen):
    screen.fill(BG_COLOR)

    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 40)

    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH//2, HEIGHT//2 -150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, WHITE)
    med_text = button_font.render("Medium", 0, WHITE)
    hard_text = button_font.render("Hard", 0, WHITE)

    quit_text = button_font.render("Quit", 0, WHITE)

    # Initialize button Background color and text
    # Easy button
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    # Medium button
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(LINE_COLOR)
    med_surface.blit(med_text, (10, 10))

    # Hard button
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Quit button
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangles
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 2 + 50))
    med_rectangle = med_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 2 + 50))
    quit_rectangle = quit_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Select difficulty from buttons
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

def draw_board(screen):
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
          
def draw_numbers(screen):
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

    #Draw sketched numbers (ana's changes)
    sketch_font = pygame.font.Font(None, SKETCH_FONT)
    sketch_surfaces = {n: sketch_font.render(str(n), 0, SKETCH_COLOR) for n in range(1, 10)}

    for (row, col), num in sketched_numbers.items():
        sketch_rect = sketch_surfaces[num].get_rect(center=(col * BOX_SIZE + BOX_SIZE // 2, row * BOX_SIZE + BOX_SIZE // 2))
        screen.blit(sketch_surfaces[num], sketch_rect)

def select_box(screen, col, row):
    # Function to highlight the user-selected box. Box will remain highlighted and may be selected again.
    #added global variables (ana's changes)
    global selected_row, selected_col
    selected_row, selected_col = row, col

    select_surface = pygame.Surface(size=(BOX_SIZE - 2, BOX_SIZE - 2))
    select_surface.fill(SELECT_COLOR)
    screen.blit(select_surface, (col * BOX_SIZE + 1, row * BOX_SIZE + 1))
    pygame.display.update()

def fill_box(screen, num, row, col):
    #ana's changes
    if (row, col) in sketched_numbers:
        del sketched_numbers[(row, col)]

    #ana's changes
    pygame.draw.rect(screen, BG_COLOR, (col * BOX_SIZE + 2, row * BOX_SIZE + 2, BOX_SIZE - 4, BOX_SIZE - 4))

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

#addition of sketch function (ana's changes)
def sketch(screen, num, row, col):
    sketched_numbers[(row, col)] = num

    sketch_font = pygame.font.Font(None, SKETCH_FONT)
    sketch_surf = sketch_font.render(str(num), 0, SKETCH_COLOR)
    sketch_rect = sketch_surf.get_rect(center=(col * BOX_SIZE + BOX_SIZE // 2, row * BOX_SIZE + BOX_SIZE // 2))

    pygame.draw.rect(screen, BG_COLOR, (col * BOX_SIZE + 2, row * BOX_SIZE + 2, BOX_SIZE - 4, BOX_SIZE - 4))
    draw_numbers(screen)

    screen.blit(sketch_surf, sketch_rect)

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
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    menu_surf = game_over_font.render("Press M to return to the main menu...", 0, LINE_COLOR)
    menu_rect = menu_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)

    pygame.display.update()

#reset, restart, & exit buttons(ana's changes)
def draw_buttons(screen):
    button_font = pygame.font.Font(None, 40)

    reset_text = button_font.render("Reset", 0, WHITE)
    restart_text = button_font.render("Restart", 0, WHITE)
    exit_text = button_font.render("Exit", 0, WHITE)

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT + 40))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT + 40))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT + 40))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()

    return reset_rectangle, restart_rectangle, exit_rectangle

#have the arrow keys switch from empty box to empty box (ana's changes; could need some work maybe idk)
def handle_arrow_keys(screen, key):
    global selected_row, selected_col
    if selected_row is None or selected_col is None:
        selected_row, selected_col = 0, 0
    else:
        original_row, original_col = selected_row, selected_col
        while True:
            if key == pygame.K_UP:
                selected_row = (selected_row - 1) % SIZE
            elif key == pygame.K_DOWN:
                selected_row = (selected_row + 1) % SIZE
            elif key == pygame.K_LEFT:
                selected_col = (selected_col - 1) % SIZE
            elif key == pygame.K_RIGHT:
                selected_col = (selected_col + 1) % SIZE
            if board[selected_row][selected_col] == 0:
                break
            if selected_row == original_row and selected_col == original_col:
                break
    select_box(screen, selected_col, selected_row)

#a lot of format change !!! (ana's changes)
def main_game_loop():
    #include global variables (ana's changes)
    global board, initial_board, selected_row, selected_col, sketched_numbers
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
    pygame.display.set_caption("Sudoku")

    while True:
        game_over = False
        completed = False
        correct = True
        #ana's changes
        sketched_numbers.clear()
        return_to_menu = False

        difficulty = draw_game_start(screen)
        if difficulty == "easy":
            board = generate_sudoku(9, 30)
        elif difficulty == "medium":
            board = generate_sudoku(9, 40)
        elif difficulty == "hard":
            board = generate_sudoku(9, 50)

        #ana's changes
        initial_board = [row[:] for row in board]
        screen.fill(BG_COLOR)
        draw_board(screen)
        draw_numbers(screen)
        #ana's changes
        reset_rectangle, restart_rectangle, exit_rectangle = draw_buttons(screen)

        #ana's changes
        while not completed and not return_to_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    #ana's changes
                    if reset_rectangle.collidepoint(x, y):
                        board = [row[:] for row in initial_board]
                        sketched_numbers.clear()
                        selected_row, selected_col = None, None
                        screen.fill(BG_COLOR)
                        draw_board(screen)
                        draw_numbers(screen)
                        reset_rectangle, restart_rectangle, exit_rectangle = draw_buttons(screen)
                    elif restart_rectangle.collidepoint(x, y):
                        completed = True
                    elif exit_rectangle.collidepoint(x, y):
                        sys.exit()
                    elif y < HEIGHT:
                        row = int(y // BOX_SIZE)
                        col = int(x // BOX_SIZE)
                        if board[row][col] == 0:
                            select_box(screen, col, row)
                if event.type == pygame.KEYDOWN:
                    #ana's changes
                    if selected_row is not None and selected_col is not None:
                        #insert return function maybe idk(im losing my mind)
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            if event.key == pygame.K_1:
                                sketch(screen, 1, selected_row, selected_col)
                            elif event.key == pygame.K_2:
                                sketch(screen, 2, selected_row, selected_col)
                            elif event.key == pygame.K_3:
                                sketch(screen, 3, selected_row, selected_col)
                            elif event.key == pygame.K_4:
                                sketch(screen, 4, selected_row, selected_col)
                            elif event.key == pygame.K_5:
                                sketch(screen, 5, selected_row, selected_col)
                            elif event.key == pygame.K_6:
                                sketch(screen, 6, selected_row, selected_col)
                            elif event.key == pygame.K_7:
                                sketch(screen, 7, selected_row, selected_col)
                            elif event.key == pygame.K_8:
                                sketch(screen, 8, selected_row, selected_col)
                            elif event.key == pygame.K_9:
                                sketch(screen, 9, selected_row, selected_col)
                        else:
                            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                                handle_arrow_keys(screen, event.key)
                            elif event.key == pygame.K_1:
                                fill_box(screen, 1, selected_row, selected_col)
                            elif event.key == pygame.K_2:
                                fill_box(screen, 2, selected_row, selected_col)
                            elif event.key == pygame.K_3:
                                fill_box(screen, 3, selected_row, selected_col)
                            elif event.key == pygame.K_4:
                                fill_box(screen, 4, selected_row, selected_col)
                            elif event.key == pygame.K_5:
                                fill_box(screen, 5, selected_row, selected_col)
                            elif event.key == pygame.K_6:
                                fill_box(screen, 6, selected_row, selected_col)
                            elif event.key == pygame.K_7:
                                fill_box(screen, 7, selected_row, selected_col)
                            elif event.key == pygame.K_8:
                                fill_box(screen, 8, selected_row, selected_col)
                            elif event.key == pygame.K_9:
                                fill_box(screen, 9, selected_row, selected_col)

            if 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 0 not in board[3] and 0 not in board[4] and 0 not in board[5] and 0 not in board[6] and 0 not in board[7] and 0 not in board[8]:
                completed = True
                correct = validate(board)
                draw_game_over(screen, correct)
                pygame.display.update()

                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            return_to_menu = True
                            break

            pygame.display.update()

        if return_to_menu:
            continue

if __name__ == "__main__":
    main_game_loop()

