class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[1] * N for _ in range(N)]
        
        for x, y in mines:
            grid[x][y] = 0
        
        upCache = [[0] * N for _ in range(N)]
        downCache = [[0] * N for _ in range(N)]
        leftCache = [[0] * N for _ in range(N)]
        rightCache = [[0] * N for _ in range(N)]
        
        for y in range(N):
            upCache[0][y] = grid[0][y]
        
            # start at x, y, and then go down
            for x in range(1, N):
                if grid [x][y] == 1:
                    upCache[x][y] += upCache[x - 1][y] + 1
                else:
                    upCache[x][y] = 0
        
        for y in range(N):
            downCache[N - 1][y] = grid[N-1][y]
        
            for x in range(N-2, -1, -1):
                if grid [x][y] == 1:
                    downCache[x][y] += downCache[x + 1][y] + 1
                else:
                    downCache[x][y] = 0
        
        for x in range(N):
            leftCache[x][0] = grid [x][0]
            
            for y in range(1, N):
                if grid[x][y] == 1:
                    leftCache[x][y]  += leftCache[x][y - 1] + 1
                else:
                    leftCache[x][y] = 0
        
        for x in range(N):
            rightCache[x][N - 1] = grid[x][N - 1]
            
            for y in range(N-2, -1, -1):
                if grid[x][y] == 1:
                    rightCache[x][y] += rightCache[x][y + 1] + 1
                else:
                    rightCache [x][y] = 0
        best = 0
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    upMax = upCache[x][y]
                    leftMax = leftCache[x][y]
                    rightMax  = rightCache[x][y]
                    downMax = downCache[x][y]
                    
                    best = max(best, min(upMax, leftMax, rightMax, downMax))
        return best