from gameObj import GameObj
import numpy
import csv


class Board:

    def __init__(self, mapSize):

        self.mapSize = mapSize

        self.grid = numpy.ndarray(shape=(mapSize), dtype=object)

        # for number in range(0, 20):
        #     self.grid[number][0] = GameObj(number, 0, "coin")
        # for number in range(0, 20):
        #     self.grid[number][19] = GameObj(number, 19, "coin")
        # for number in range(0, 20):
        #     self.grid[0][number] = GameObj(0, number, "coin")
        # for number in range(0, 20):
        #     self.grid[19][number] = GameObj(19, number, "coin")
        #
        # for number in range(0, 20):
        #     self.grid[number][6] = GameObj(number, 6, "coin")
        # for number in range(0, 20):
        #     self.grid[number][14] = GameObj(number, 14, "coin")
        # for number in range(0, 20):
        #     self.grid[6][number] = GameObj(6, number, "coin")
        # for number in range(0, 20):
        #     self.grid[14][number] = GameObj(14, number, "coin")
        #
        # self.grid[0][0] = GameObj(0, 0, "player")
        #
        # for i in range(len(self.grid)):
        #     for j in range(len(self.grid[i])):
        #         if self.grid[i][j] is None:
        #             self.grid[i][j] = GameObj(i, j, "brick")

        # self.grid[17][10] = GameObj(17, 10, "brick")
        # self.grid[14][10] = GameObj(14, 10, "coin")

        self.playerX = 0
        self.playerY = 0

    # def populate(for i in range(len(self.grid)):self):
    #     playerObjXY = [2, 2]
