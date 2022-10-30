class TreeNode:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.depth = 0
        self.h = 0
        self.up = None
        self.down = None
        self.left = None
        self.right = None
