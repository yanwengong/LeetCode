## number of islands
## the bfs method
## https://leetcode.com/problems/number-of-islands/
## https://www.geeksforgeeks.org/islands-in-a-graph-using-bfs/

class Solution:
    ## check whether the element can be used to run bfs
    def check_bfs(self, i, j, visited, grid):
        if (i >=0 and i < len(grid) and j >=0 and j < len(grid[0]) and
        visited[i][j] == 0 and grid[i][j] == "1"):
            return True

    ## dfs function: once find a element to label as 1, label all its neibor
    def bfs(self, i, j, visited, grid):
        visited[i][j] = 1

        neibor_row = [-1, 0, 0, 1]
        neibow_col = [0, -1, 1, 0]

        q_lst = []
        q_lst.append([i,j])

        while len(q_lst)!= 0:
            pair = q_lst.pop(-1)
            new_i = pair[0]
            new_j = pair[1]

            for k in range(len(neibor_row)):
                if self.check_bfs(new_i + neibor_row[k], new_j + neibow_col[k], visited, grid):
                    visited[new_i + neibor_row[k]][new_j + neibow_col[k]] = 1
                    q_lst.append([new_i + neibor_row[k], new_j + neibow_col[k]])


    ## this is the main function
    def numIslands(self, grid: List[List[str]]) -> int:

        ## corner case:
        if grid == []: return 0

        count = 0
        num_row = len(grid)
        num_col = len(grid[0])

        visited = [[0 for i in range(num_col)] for j in range(num_row)]

        for i in range (num_row):
            for j in range(num_col):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    self.bfs(i, j, visited, grid)
                    count += 1

        return count
