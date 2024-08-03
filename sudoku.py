#main function for the game
import pygame, sys
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
        pygame.draw.line(screen, LINE_COLOR, (0, i*BOX_SIZE), (WIDTH, i*BOX_SIZE), LINE_WIDTH)

    #Draw vertical lines
    for i in range(1, SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i*BOX_SIZE, 0), (i*BOX_SIZE, HEIGHT), LINE_WIDTH)

def draw_numbers():
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

def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if completed:
        text = "Level Completed"
    else:
        text = "Level Failed"

    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over.surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    restart_surf = game_over_font.render("Press R to restart the level...", 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
    screen.blit(restart_surf, restart_rect)

    menu_surf = game_over_font.render("Press M to return to the main menu...")
    menu_rect = menu_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 150))
    screen.blit(menu_surf, menu_rect)

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    game_over = False
    completed = False

    difficulty = draw_game_start(screen)
    if difficulty == "easy":
        board = generate_sudoku(9, 30)
    elif difficulty == "medium":
        board = generate_sudoku(9, 50)
    elif difficulty == "hard":
        board = generate_sudoku(9, 70)

    screen.fill(BG_COLOR)
    draw_board()
    draw_numbers()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not completed:
                x, y = event.pos
                row = y // BOX_SIZE
                col = x // BOX_SIZE


        pygame.display.update()








