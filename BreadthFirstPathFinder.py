from random import shuffle

class BreadthFirstPathFind:
    '''
    \nPathfinding class using a breadth first method
    \nInputs on init:
    \n - board : list of lists, 1's representing boundaries
    \n - POI : points of interest -> [[start], [end]]
    \n\t\t\t\t\t\t-> [start] : [startrow, startcol]
    \n\t\t\t\t\t\t-> [end] : [endrow, endcol]
    \n - illustrate : boolean to show results
    '''
    def __init__(self, board, POI, illustrate):
    
        # Get board and copy to illustrate
        self.board = board
        self.draw = board

        # Get start and end points
        self.start, self.end = POI
        
        # Get shortest path on init
        self.shortestpath = self.breadthfirst()  

        # No Possible Solution:
        if self.shortestpath == None:
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

    def GetMoves(self, point):
        '''
        \nGet move indices surrounding current point.
        \nInputs:
        \n - point : [x, y]
        \nReturns:
        \n - moves : [[top], [right], [bottom], [left]]
        '''
        
        # Separate point and find surrounding indices
        x, y, = point
        # "North, East, South, West"
        n = [x, y + 1]
        e = [x + 1, y]
        s = [x, y - 1]
        w = [x - 1, y]

        # Assemble and return output
        moves = [n, e, s, w]
    
        return moves
    
    def breadthfirst(self):
        '''
        \nMethod to return shortest path using breadth first algorithm
        \nOutputs:
        \n - currentpath : list of lists of points comprising the shortest path
        \n\t OR None if no path is possible
        '''

        # Add start point to search path and to visited points
        searchpaths = [[self.start]]
        visited = [self.start]

        # Searchpaths is empty when best path is found. Loop till complete.
        while searchpaths != []:
            print(searchpaths)
            print(len(searchpaths))
            print()

            # Get last element of searchpaths
            currentpath = searchpaths.pop(0)
            # Last coord of current path is current coord
            currentcoord = currentpath[-1]
            
            # Found End
            if currentcoord == self.end:
                # Return successful path
                return currentpath

            # Check positions surrounding    
            for nextcoord in self.GetMoves(currentcoord):

                nx, ny = nextcoord
                
                # Skip out of bounds
                if nx < 0  or nx > (len(self.board[0]) -1):
                    continue
                if ny < 0  or ny > (len(self.board) -1):
                    continue

                # Skip visited
                if nextcoord in visited:
                    continue

                # Skip walls
                if self.board[nx][ny] == 1:
                    continue

                # Still in loop implies a valid position
                searchpaths.append(currentpath + [nextcoord])
                # Mark as visited
                visited += [nextcoord]
        
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
            for coord in self.shortestpath:

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
    sample = [
              [1, 0, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 0, 1]
              ]
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
    starts = [0, 1]
    ends = [5, 4]

    startm = [0, 1]
    endm = [8, 7]

    startb = [0, 1]
    endb = [11, 10]

    POIs = [starts,ends]
    POIm = [startm, endm]
    POIb = [startb, endb]

    p = BreadthFirstPathFind(midsample, POIm, True)