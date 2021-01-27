## topological order
## https://en.wikipedia.org/wiki/Topological_sorting
## the vertices of the graph may represent tasks to be performed,
## and the edges may represent constraints that one task must be performed before another
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        selhttps://www.lintcode.com/en/old/problem/topological-sorting/#f.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def findRoot(self, input_graph):
        child_lst = []
        for i in input_graph:
            for j in i.neighbors:
                child_lst.append(j)

        ## return diff between input_graph and child_lst
        return(list(set(input_graph) - set(child_lst)))

    def topSort(self, graph):
        order_lst = self.findRoot(graph)

        temp_queue = list(set(graph) - set(order_lst))

        while len(temp_queue) != 0:
            new_root = self.findRoot(temp_queue)
            order_lst.append(new_root)
            temp_queue = list(set(temp_queue) - set(new_root))

        return(order_lst)


## another method
## create a map dictionary to store each node as key and num of parents of val
## create a visited set
## use BFS is map == 0 & not in visited
## BFS will iterate within its neibor and update neighbors' val and vistied
