## count the shortest path in an unweighted graph
## https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
## change from the website above: instead of output the exact path, output the number of node contained in the path


# Definition for an unweighted graph
# class GraphNode:
#     def __init__(self, x):
#         self.val = x
#         self.neibors = None

class Solution:
    def num_short_path(self, start:GraphNode, end:GraphNode) -> int:
        if start.val == end.val: return 0

        count = 0
        node_lst = [start]
        val_lst = [start.val]


        while end.val not in val_lst:
            count += 1
            neibor_lst = []
            val_lst = []
            for i in node_lst:
                neibor_lst.append(i.neibor)
            for j in neibor_lst:
                val_lst.append(j.val)


            ## deal with if end val is not in the graph
            if val_lst == []:
                return -1

            node_lst = neibor_lst

        return count



class Solution_ch:
    def shortestPath(start, end):
        counter = 0
        ## use set, thus when check "not in" it's O(1)
        visited = set()
        curr_level = [start]
        next_level = []
        while len(curr_level) > 0 or len(next_level) > 0:
            ## curr_level has all been poped out, set curr as next, empty next, counter += 1
            if len(curr_level) == 0:
                curr_level = next_level
                next_level = []
                counter += 1

            node = curr_level.pop(0)
            if node.value == end.value:
                return counter

            ## mark each visited node, avoid fall into circle
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    next_level.append(neighbor)

        return -1
