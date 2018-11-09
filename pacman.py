# #This is the Repo Test File
# # Test2
# import pygame, sys, os, random
# from pygame.locals import *
#
# pygame.init()
# window = pygame.display.set_mode((500, 500))

# Import a library of functions called 'pygame'
import pygame
import csv
import thorpy
from math import pi
from Board import Board
from gameObj import GameObj

# from splash import drawSplash

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [1000, 1000]
screen = pygame.display.set_mode(size)
score = 0
board = Board((20, 20))


def saveFile(board):
    with open('savefile.csv', mode='w') as save_file:
        writer = csv.writer(save_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(board.grid)):
            new_row = []
            for j in range(len(board.grid[i])):
                if board.grid[i][j].type == "empty":
                    new_row.append("empty")
                if board.grid[i][j].type == "brick":
                    new_row.append("brick")
                elif board.grid[i][j].type == "coin":
                    new_row.append("coin")
                elif board.grid[i][j].type == "player":
                    new_row.append("player")
            writer.writerow(new_row)


def readFile():
    with open('savefile.csv', mode='r') as read_file:
        reader = csv.reader(read_file, delimiter=',')
        line_count = 0
        for row in reader:
            for j, obj in enumerate(row):
                # obj = reader[i][j]
                board.grid[line_count][j] = GameObj(line_count, j, obj)
                print(board.grid[line_count][j])
            line_count += 1

def move(board, direction):
    directionDeltas = {
        "null": [0, 0],
        "U": [0, -1],
        "D": [0, 1],
        "L": [-1, 0],
        "R": [1, 0]
    }

    global score

    # player = board.grid[board.playerX][board.playerY]
    # print(player)

    targetX = board.playerX + directionDeltas[direction][0]
    targetY = board.playerY + directionDeltas[direction][1]

    if ((targetX >= 0 and targetX < board.mapSize[0]) and (targetY >= 0 and targetY < board.mapSize[1])):
        if board.grid[targetX][targetY].type == "empty":
            board.grid[board.playerX][board.playerY] = GameObj(board.playerX, board.playerY, "empty")
            board.playerX = targetX
            board.playerY = targetY
        elif board.grid[targetX][targetY].type == "coin":
            board.grid[board.playerX][board.playerY] = GameObj(board.playerX, board.playerY, "empty")
            board.playerX = targetX
            board.playerY = targetY
            score += 1

        # if board.grid[targetX][targetY].type == "coin":

        # print(board.playerX)
        # print(board.playerY)
        # #
        # player.x = board.playerX
        # player.y = board.playerY

    board.grid[board.playerX][board.playerY] = GameObj(board.playerX, board.playerY, "player")


def drawSplash():
    # readFile()
    # Declaration of the application in which the menu is going to live.
    application = thorpy.Application(size=(500, 500), caption='ThorPy stupid Example')

    # Setting the graphical theme. By default, it is 'classic' (windows98-like).
    thorpy.theme.set_theme('human')

    # Declaration of some elements...
    global board
    useless1 = thorpy.make_button("This button is useless.\nAnd you can't click it.")

    text = "This button also is useless.\nBut you can click it anyway."
    useless2 = thorpy.Clickable.make(text)

    draggable = thorpy.Draggable.make("Drag me!")

    box1 = thorpy.make_ok_box([useless1, useless2, draggable])
    options1 = thorpy.make_button("Some useless things...")
    thorpy.set_launcher(options1, box1)

    inserter = thorpy.Inserter.make(name="Tip text: ",
                                    value="This is a default text.",
                                    size=(150, 20))

    file_browser = thorpy.Browser.make(path="C:/Users/", text="Please have a look.")

    browser_launcher = thorpy.BrowserLauncher.make(browser=file_browser,
                                                   const_text="Choose a file: ",
                                                   var_text="")

    color_setter = thorpy.ColorSetter.make()
    color_launcher = thorpy.ColorSetterLauncher.make(color_setter,
                                                     "Launch color setter")

    options2 = thorpy.make_button("Useful things")
    box2 = thorpy.make_ok_box([inserter, color_launcher, browser_launcher])
    thorpy.set_launcher(options2, box2)

    quit_button = thorpy.make_button("Quit")
    quit_button.set_as_exiter()

    central_box = thorpy.Box.make([options1, options2, quit_button])
    central_box.set_main_color((200, 200, 200, 120))
    central_box.center()

    # Declaration of a background element - include your own path!
    background = thorpy.Background.make(image=thorpy.style.EXAMPLE_IMG,
                                        elements=[central_box])

    menu = thorpy.Menu(elements=background, fps=45)
    menu.play()



def main():
    # Initialize the game engine
    pygame.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    global score
    global board
    clock = pygame.time.Clock()


    # print(board.grid)

    pygame.key.set_repeat()

    # Loop until the user clicks the close button.
    done = False

    # saveFile(board)
    readFile()

    while not done:

        playing = True
        splash = False

        if splash:
            status = drawSplash()
            if status == "play":
                playing = True

        while playing:
            screen.fill(WHITE)

            textsurface = myfont.render('Score: ' + str(score), False, RED, BLACK)
            screen.blit(textsurface, (0, 0))

            for i in range(len(board.grid)):
                for j in range(len(board.grid[i])):
                    if board.grid[i][j] != None:
                        cell = board.grid[i][j]
                        # print("obj found")
                        # print(cell.x)
                        # print(cell.y)
                        # pygame.draw.rect(screen, BLACK, [cell.X*50, cell.Y*50, 50, 20],2)
                        if (cell.type == "player"):
                            pygame.draw.rect(screen, BLACK, [cell.x * 50, cell.y * 50, 50, 50])
                        elif (cell.type == "brick"):
                            pygame.draw.rect(screen, RED, [cell.x * 50, cell.y * 50, 50, 50])
                        elif (cell.type == "coin"):
                            pygame.draw.rect(screen, BLUE, [cell.x * 50 + 20, cell.y * 50 + 20, 10, 10])

                        # pygame.draw.rect(screen, BLACK, [500, 500, 50, 20], 2)

            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(10)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                move(board, "U")
            if keys[pygame.K_DOWN]:
                move(board, "D")
            if keys[pygame.K_LEFT]:
                move(board, "L")
            if keys[pygame.K_RIGHT]:
                move(board, "R")

            for event in pygame.event.get():  # User did something

                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                # elif event.type == pygame.KEYDOWN:

                # keys = pygame.key.get_pressed()
                #
                # if keys[pygame.K_UP]:
                #     move("U")
                # if keys[pygame.K_DOWN]:
                #     move("D")
                # if keys[pygame.K_LEFT]:
                #     move("L")
                # if keys[pygame.K_RIGHT]:
                #     move("R")

                # if (event.key == pygame.K_LEFT):
                #     move("L")
                #
                # elif (event.key == pygame.K_RIGHT):
                #     move("R")
                # elif (event.key == pygame.K_UP):
                #     move("U")
                # elif (event.key == pygame.K_DOWN):
                #     move("D")

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()


if __name__ == "__main__":
    main()
