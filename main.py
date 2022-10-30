import heapq as heap
import TreeNode

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
        uniform(puzzle)
    elif algorithm == "2":
        misplaced(puzzle)
    elif algorithm == "2":
        manhattan(puzzle)


def generalsearch(problem, quefunc):
    # make a queue of nodes
    nodes = [TreeNode(problem.init)]
    while nodes:
        # if queue is empty return fail
        if nodes == 0:
            return "failure"
        # else queue pop the front
        node = nodes.pop(0)
        # if node is at goal state return it
        if goal(nodes):
            return node
        # else run the search on the algo again
        nodes = quefunc(nodes, expand(node, problem.OPERATORS))


def expand(node, ops)


main()
