import TreeNode
import copy

# Copied this menu & default system from the example code from Project 1

solved = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]
easy = [[1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]]
medium = [[1, 2, 0],
          [4, 5, 3],
          [7, 8, 6]]
hard = [[0, 1, 2],
        [4, 5, 3],
        [7, 8, 6]]
impossible = [[8, 6, 7],
              [2, 5, 4],
              [3, 0, 1]]


def main():
    puzzle_mode = input(
        "Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
        algo(default_puzzle())

    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " +
              "the numbers with a space. RET only when finished." + '\n')
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")

        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])

        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        algo(user_puzzle)
    return


def default_puzzle():
    selected_difficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 4." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return solved
    elif selected_difficulty == "1":
        print("Difficulty of 'Easy' selected.")
        return easy
    elif selected_difficulty == "2":
        print("Difficulty of 'Medium' selected.")
        return medium
    elif selected_difficulty == "3":
        print("Difficulty of 'Hard' selected.")
        return hard
    elif selected_difficulty == "4":
        print("Difficulty of 'Impossible' selected.")
        return impossible


def print_puzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')


def algo(puzzle):
    algorithm = input(
        "Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, " "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        generalsearch(TreeNode.TreeNode(puzzle, 0))


def generalsearch(problem):
    # make a queue of nodes
    nodes = []
    # count of nodes
    numNodes = 0
    # max queue size
    mqz = 0
    # to avoid duplicate nodes
    used_nodes = []
    # put the first node into the queue
    nodes.append(problem)

    while nodes:
        # if queue is empty return fail
        if not nodes:
            return False
        # else queue pop the front
        node = nodes.pop(0)
        # expand by 1
        numNodes += 1
        # update max queue size with larger between itself and length of curr queue
        mqz = max(len(nodes), mqz)
        # if node is at goal state return it
        if goal(node.puzzle):
            print("Depth of solution: " + str(node.depth))
            print("Number of nodes expanded: " + str(numNodes))
            print("Max queue size: " + str(mqz))
            return node
        # else run the search on the algo again
        # make sure it hasn't been seen before
        if node not in used_nodes:
            # nodes = quefunc(nodes, expand(node))
            # adding this to duplicated node list
            used_nodes.append(copy.deepcopy(node))


def expand(node):
    nodes = []

    up_node = node.moveUp()
    nodes.append(up_node)
    node.children.append(up_node)

    down_node = node.moveDown()
    nodes.append(down_node)
    node.children.append(down_node)

    left_node = node.moveLeft()
    nodes.append(left_node)
    node.children.append(left_node)

    right_node = node.moveRight()
    nodes.append(right_node)
    node.children.append(right_node)

    return nodes


def goal(puzzle):
    ans = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
    if puzzle == ans:
        return True
    return False


main()
