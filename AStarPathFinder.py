import heapq

class Node():
    """Node class for A* pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

class AStarPathFind:
    def __init__ (self, board, POI, illustrate = False, diags = True):
        self.board = board
        self.draw = board

        # Allow diagonal movement?
        self.diags = diags

        self.POI = POI
        self.start, self.end = POI

        self.path = self.astar()

        if self.path == None:
            # Illustrate unsolved board and print error message
            illustrate = False

            print("\nUnsolved:\n")

            self.illustrate(self.board)

            print("\nError! No solution found.\n")
        
        # Illustrate
        if illustrate == True:
            # Illustrate unsolved and solved boards in terminal
            print("\nUnsolved:\n")
            self.illustrate(self.board)
            print()

            print("\nSolved:\n")
            self.illustratePath()
            print('\n')

    def returnPath(self, current_node):
        path = []
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]
    
    def astar(self):

        # Create start and end nodes
        start_node = Node(None, self.start)
        start_node.g = start_node.h = start_node.f = 0

        end_node = Node(None, self.end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize open and closed lists
        open_list = []
        closed_list = []

        # Heapify lists... smallest element returned first, others unsorted
        heapq.heapify(open_list)
        heapq.heappush(open_list, start_node)

        # Stop condition
        outer_iter = 0
        max_iter = (len(self.board[0]) * len(self.board)//2)

        # Allow diagonal movement?
        if self.diags == True:
            adj = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)
        else:
            adj = ((0, -1), (0, 1), (-1, 0), (1, 0),)

        # Loop until you reach the end
        while len(open_list) > 0:
            outer_iter += 1
            # print("OuterIter: " + str(outer_iter))

            if outer_iter > max_iter:
                print("\nToo many iterations... Quitting.\n")
                return self.returnPath(current_node)
            
            # Get current node
            current_node = heapq.heappop(open_list)
            closed_list.append(current_node)

            # current_index = 0
            # Found goal
            if current_node == end_node:
                return self.returnPath(current_node)
            
            # Generate children
            children = []

            for new_position in adj:

                # Get node position
                node_position = (current_node.position[0] + new_position[0] , current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(self.board) - 1) or node_position[0] < 0 or node_position[1] > (len(self.board[len(self.board) - 1 ]) - 1) or node_position[1] < 0:
                    continue

                # Walkable terrain
                if self.board[node_position[0]][node_position[1]] != 0:
                    continue
                
                # Create a new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                    continue
            
                # Create f, g, and h values
                child.g = current_node.g + 1
                child.h = (child.position[0] - end_node.position[0])**2 + (child.position[1] - end_node.position[1])**2
                child.f = child.g + child.h

                # Child is on the open list
                if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                    continue

                heapq.heappush(open_list, child)
        
        # If no path is found, print error and return None
        print("Couldn't find a path to destination.")
        return None

    def illustrate(self, lsts):
        '''
        Print out items from lists, and replace zeros with spaces
        '''
        
        for lst in lsts:
            for itm in lst:
                if itm == 0: itm = " "
                print(str(itm), end=' ')
            print()
    
    def illustratePath(self):
        '''
        Illustrate the shortest path to the end goal
        '''

        try:
            # If result is not None, replace traveled coordinates with *
            for coord in self.path:

                # Separate coordinate
                x, y = coord

                # Denote start, end, and path
                if coord == self.start: self.draw[x][y] = "s"
                elif coord == self.end: self.draw[x][y] = "e"
                else: self.draw[x][y] = '*'
            
            # Illustrated updated board
            self.illustrate(self.draw)
        except:
            # If no solution is available, print error
            print("\nNo solution found to illustrate...\n")
            return -1

if __name__ == "__main__":
    test = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
    teststart = (0, 0)
    testend = (7, 6)
    testPOI = [teststart, testend]

    smallsample = [
              [1, 0, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 0, 1]
              ]
    smallstart = (0, 1)
    smallend = (5, 4)
    smallPOI = [smallstart, smallend]

    midsample = [
              [1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 0, 1, 1, 1],
              [1, 0, 1, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 1, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0, 1]
              ]
    midstart = (0, 1)
    midend = (8, 7)
    midPOI = [midstart, midend]

    bigsample = [
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
                ]
    bigstart = (0, 1)
    bigend = (11, 10)
    bigPOI = [bigstart, bigend]

    hugesample =[
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
                [0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,] * 2,
                [0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,] * 2,
                [0,0,0,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,] * 2,
                [0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,] * 2,
                [0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,] * 2,
                [0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,] * 2,
                [0,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,] * 2,
                [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,] * 2,
                [0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,] * 2,
                [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,] * 2,
                [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,] * 2,
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,] * 2,
                ]
    hugestart = (0, 0)
    hugeend = (len(hugesample) - 1, len(hugesample[0]) - 1)
    hugePOI = [hugestart, hugeend]

    def printsep():
        print("--------------------------------------------")

    t1 = AStarPathFind(test, testPOI, True)
    printsep()
    t2 = AStarPathFind(smallsample, smallPOI, illustrate=True)
    printsep()
    t3 = AStarPathFind(midsample, midPOI, illustrate=True)
    printsep()
    t4 = AStarPathFind(bigsample, bigPOI, illustrate=True)
    printsep()
    t5 = AStarPathFind(hugesample, hugePOI, illustrate=True)