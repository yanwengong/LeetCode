## Network delay time
## Dijkstra's algorithm
## https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        ## init a distance array
        dist_array = [float("inf")]*(N)
        dist_array[K-1] = 0

        ## init a visted dist_array
        v = [K]

        ## init a parent dict, key is node, value is parent
        #p = {}
        #p[K] = "root"

        ## init Q
        Q = [K]

        while len(Q) != 0:
            element = Q.pop(0)
            #print(element)

            for i in range(len(times)):
               # print(i)
                element1 = times[i][0]
                if element != element1 and element1 not in v and element1 not in Q:
                    Q.append(element1)
                else:
                    element2 = times[i][1]
                    new_dist = times[i][2] + dist_array[element1 - 1]
                    if new_dist < dist_array[element2 - 1]:
                        dist_array[element2 - 1] = new_dist
                        v.append(element2)
                        #p[element2] = element1
                        #Q.append(element2)
                        #times.remove(times[i])
                        #print(i)
                       # print(times)

        #print(dist_array)
        for i in dist_array:
            if i == inf:
                return -1

        return max(dist_array)
