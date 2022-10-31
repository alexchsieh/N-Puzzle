import copy


class TreeNode:

    def __init__(self, puzzle, depth):
        self.puzzle = puzzle
        self.depth = depth
        self.h = 0
        self.children = []

    def moveUp(self):
        x = 0
        y = 0

        # identify where the 0 is
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == 0:
                    x = i
                    y = j

        # check edge cases
        if x == 0:
            return

        #deepcopy and swap
        newpuzzle = copy.deepcopy(self)
        temp = newpuzzle.puzzle[x-1][y]
        newpuzzle.puzzle[x-1][y] = newpuzzle.puzzle[x][y]
        newpuzzle.puzzle[x][y] = temp
        return newpuzzle

    def moveLeft(self):
        x = 0
        y = 0

        # identify where the 0 is
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == 0:
                    x = i
                    y = j

        # check edge cases
        if y == 0:
            return

        #deepcopy and swap
        newpuzzle = copy.deepcopy(self)
        temp = newpuzzle.puzzle[x][y-1]
        newpuzzle.puzzle[x][y-1] = newpuzzle.puzzle[x][y]
        newpuzzle.puzzle[x][y] = temp
        return newpuzzle

    def moveDown(self):
        x = 0
        y = 0

        # identify where the 0 is
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == 0:
                    x = i
                    y = j

        # check edge cases
        if x == 2:
            return

        #deepcopy and swap
        newpuzzle = copy.deepcopy(self)
        temp = newpuzzle.puzzle[x-1][y]
        newpuzzle.puzzle[x-1][y] = newpuzzle.puzzle[x][y]
        newpuzzle.puzzle[x][y] = temp
        return newpuzzle

    def moveRight(self):
        x = 0
        y = 0

        # identify where the 0 is
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == 0:
                    x = i
                    y = j

        # check edge cases
        if y == 2:
            return

        #deepcopy and swap
        newpuzzle = copy.deepcopy(self)
        temp = newpuzzle.puzzle[x][y+1]
        newpuzzle.puzzle[x][y+1] = newpuzzle.puzzle[x][y]
        newpuzzle.puzzle[x][y] = temp
        return newpuzzle
