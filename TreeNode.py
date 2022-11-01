import copy


class TreeNode:

    def __init__(self, puzzle):
        # changed depth to not be a parameter
        self.puzzle = puzzle
        self.depth = 0
        self.h = 0
        self.children = []
        self.expanded = False

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
            return None

        #deepcopy and swap
        up = copy.deepcopy(self.puzzle)
        temp = up[x-1][y]
        up[x-1][y] = up[x][y]
        up[x][y] = temp
        return up

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
            return None

        #deepcopy and swap
        left = copy.deepcopy(self.puzzle)
        temp = left[x][y-1]
        left[x][y-1] = left[x][y]
        left[x][y] = temp
        return left

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
            return None

        #deepcopy and swap
        down = copy.deepcopy(self.puzzle)
        temp = down[x+1][y]
        down[x+1][y] = down[x][y]
        down[x][y] = temp
        return down

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
            return None

        #deepcopy and swap
        right = copy.deepcopy(self.puzzle)
        temp = right[x][y+1]
        right[x][y+1] = right[x][y]
        right[x][y] = temp
        return right
