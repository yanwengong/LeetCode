## depth search first
## https://en.wikipedia.org/wiki/Depth-first_search
## Given a start node and another graphnode, find the shortest path from start to end

class GraphNode:
    def __init__(self):
        self.value = None
        self.neighbors = []



class Solution:
    """docstring for Solution."""

    def __init__(self, arg):
        super(Solution, self).__init__()
        self.arg = arg

    def dfs(start, end):
        ## corner case
        if start.val == end.val: return [start]

        path = []
        visited = set() # very fast to check whether element is within set
        dfs_helper(start, end, path, visited)
        return path

    def dfs_helper(start, end, path, visited):
        if start.val == end.val:
            path.append(end)
            return True

        path.append(start)
        visited.append(start)

        for x in start.neighbors:
            if x in visited:
                continue ## skip the following command and go back to for loop

            if dfs_helper(x, end, path, visited):
                True

            path.pop(-1)
            return False
