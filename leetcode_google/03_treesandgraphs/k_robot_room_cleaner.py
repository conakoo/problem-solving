# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        visited = set()
        dx = [-1, 0, 1, 0] # up, right, down, left
        dy = [0, 1, 0, -1]

        def backtrack(x, y, d):
            visited.add((x, y))
            robot.clean()
            for i in range(4):
                nd = (d+i)%4
                nx = x+dx[nd]
                ny = y+dy[nd]
                if not (nx, ny) in visited and robot.move(): # move next
                    backtrack(nx, ny, nd) # clean
                    go_back() # back to currnet
                robot.turnRight() # next direction
        
        backtrack(0, 0, 0) # assume start point as (0, 0) with direction=up
