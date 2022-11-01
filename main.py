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
    mqz = 0
    # to avoid duplicate nodes
    used_nodes = []

    # based on heuristic, get the h value
    if quefunc == 1:
        # uniform is naturally 0
        h = 0
    elif quefunc == 2:
        h = misplaced(problem)
    elif quefunc == 3:
        h = manhattan(problem)

    # making the puzzle into a node and giving initial values
    n = TreeNode.TreeNode(problem)
    n.h = h
    n.depth = 0

    # putting initial puzzle into queue
    nodes.append(n)

    # adding the puzzle to the seen list
    used_nodes.append(n.puzzle)

    while nodes:
        if quefunc != 1:
            # ASKED CLASSMATES & YOUTUBE FOR HELP
            # LAMBDA ALLOWS YOU TO PASS IN MULTIPLE ARGUMENTS FOR X TO SORT
            # IN THIS CASE IT WILL SORT BY SMALLEST DEPTH + H VALUE
            # IT WILL FALL BACK TO DEPTH ALONE IF IT TIES
            nodes = sorted(nodes, key=lambda x: (x.depth + x.h, x.depth))

        # if queue is empty return fail
        if not nodes:
            return False

        # update max queue size with larger between itself and length of curr queue
        mqz = max(len(nodes), mqz)

        # keeps popping the front node to run algorithm
        node = nodes.pop(0)

        # expand by 1
        if node.expanded is False:
            # this helps you not double count nodes
            numNodes += 1
            node.expanded = True

        # if node is at goal state return it
        print_puzzle(node.puzzle)
        print("Depth of solution: " + str(node.depth))
        if goal(node.puzzle):
            print("Depth of solution: " + str(node.depth))
            print("Number of nodes expanded: " + str(numNodes))
            # edge case, if it's the correct puzzle from the start, need to remove the initial queue size
            if mqz == 1:
                mqz -= 1
            print("Max queue size: " + str(mqz))
            return node

        # gives you all the possible children for your node
        a = expand(node, used_nodes)

        # iterates through the children
        for x in a.children:
            # makes sure that the child exists
            if x is not None:
                # if the heuristic is uniform, just increase depth by 1
                if quefunc == 1:
                    x.depth = node.depth + 1
                    x.h = 0
                # if heuristic is other, must compute h cost
                elif quefunc == 2:
                    x.depth = node.depth + 1
                    x.h = misplaced(x.puzzle)
                elif quefunc == 3:
                    x.depth = node.depth + 1
                    x.h = manhattan(x.puzzle)

                # adds the child to the queue in order of L R U D
                nodes.append(x)
                # adds the puzzle to a list of seen puzzles so you dont repeat
                used_nodes.append(x.puzzle)


def misplaced(puzzle):
    ans = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
    count = 0

    # iterate the entire puzzle
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            # check if your index is in the right place
            if int(puzzle[i][j]) != ans[i][j]:
                # check if your index is not the blank space
                if int(puzzle[i][j]) != 0:
                    # increment heuristic value by 1
                    count += 1
    return count


def expand(node, used_nodes):

    # when running the debugger, the functions were being ran 3 times per if statement
    # just calculated it once up here and can be reused way faster
    l = node.moveLeft()
    r = node.moveRight()
    u = node.moveUp()
    d = node.moveDown()

    # make sure the puzzle movement in direction is possible
    # checks if the puzzle has not been seen before
    # if both pass add the newly generated puzzle as a child of the parent node
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
    # compares puzzle to ideal puzzle and returns
    ans = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
    if puzzle == ans:
        return True
    return False


main()
