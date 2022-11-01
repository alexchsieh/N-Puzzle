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
    # instead of turning it into a node here, keep it as just the board, make node inside search
    generalsearch(puzzle, int(algorithm))


def generalsearch(problem, quefunc):
    # make a queue of nodes
    nodes = []
    # count of nodes
    numNodes = -1
    # max queue size
    mqz = -1
    # to avoid duplicate nodes
    used_nodes = []
    # put the first node into the queue

    if quefunc == 1:
        h = 0
    elif quefunc == 2:
        h = misplaced(problem)
    elif quefunc == 3:
        h = manhattan(problem)

    # making the puzzle into a node and giving initial values
    n = TreeNode.TreeNode(problem)
    n.h = h
    n.depth = 0
    nodes.append(n)
    # adding the puzzle to the seen list
    used_nodes.append(n.puzzle)

    while nodes:
        # if queue is empty return fail
        if not nodes:
            return False
        # else queue pop the front
        node = nodes.pop(0)
        # update max queue size with larger between itself and length of curr queue
        mqz = max(len(nodes), mqz)
        # expand by 1
        if node.expanded is False:
            # this helps you not double count nodes
            numNodes += 1
            node.expanded = True
        # if node is at goal state return it
        print_puzzle(node.puzzle)
        if goal(node.puzzle):
            print("Depth of solution: " + str(node.depth))
            print("Number of nodes expanded: " + str(numNodes))
            print("Max queue size: " + str(mqz))
            return node
        # else run the search on the algo again
        # make sure it hasn't been seen before
        # adding this to duplicated node list
        a = expand(node, used_nodes)

        for x in a.children:
            if x is not None:
                if quefunc == 1:
                    x.depth = node.depth + 1
                    x.h = 0
                elif quefunc == 2:
                    x.depth = node.depth + 1
                    x.h = misplaced(x.puzzle)
                elif quefunc == 3:
                    x.depth = nd.depth + 1
                    x.h = manhattan(x.puzzle)
                nodes.append(x)
                used_nodes.append(x.puzzle)


def expand(node, used_nodes):

    l = node.moveLeft()
    r = node.moveRight()
    u = node.moveUp()
    d = node.moveDown()

    if l != None:
        if l not in used_nodes:
            left_node = TreeNode.TreeNode(l)
            node.children.append(left_node)

    if r != None:
        if r not in used_nodes:
            right_node = TreeNode.TreeNode(r)
            node.children.append(right_node)

    if u != None:
        if u not in used_nodes:
            up_node = TreeNode.TreeNode(u)
            node.children.append(up_node)

    if d != None:
        if d not in used_nodes:
            down_node = TreeNode.TreeNode(d)
            node.children.append(down_node)

    return node


def goal(puzzle):
    ans = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
    if puzzle == ans:
        return True
    return False


main()
