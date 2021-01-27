## course schedule
## https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True


        pre_num = len(prerequisites) #1

        ## in dictionary, class as key, prereq as vals
        pre_dict = {}
        for i in range(pre_num):
            key = prerequisites[i][0]
            if key in pre_dict:
                pre_dict[key].append(prerequisites[i][1])
            else:
                pre_dict[key] = [prerequisites[i][1]] #pre_dict[1] = 0

        ## add the class without prerequisites into complete queue
        complete_queue = []
        for i in range(numCourses):
            if i not in pre_dict.keys():
                complete_queue.append(i)
                pre_dict[i] = [] #complete_queue = [0], pre_dict[0] = []


        ## count the complete class - start with class with no prere
        complete_num = len(complete_queue) # complete_num = 1

        while len(complete_queue) != 0:
            element = complete_queue.pop(-1) #element = 0
            for i in range(numCourses):
                if pre_dict[i] == []:
                    continue
                for val in pre_dict[i]: # val = pre_dict[1] = 0
                    if val == element:
                        pre_dict[i].remove(val) # pre_dict[1] = []
                if pre_dict[i] == []:
                    complete_queue.append(i) # complete_queue = [1, 0]
                    complete_num += 1 # complete_num = 2


        return complete_num == numCourses


## real BFS
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         if len(prerequisites) == 0:
            return True

        ## construct graphNode as dict; key is pre_req, vals are tje following clsses
        adict = {}
        for i in range(numCourses):
            adict[i] = []

        for pair in range(len(prerequisites)):
            adict[prerequisites[pair][1]].append(prerequisites[pair][0])


        ## construct indegrees array; idx is class, val is # pre_req
        indegrees = [0]*numCourses
        for pair in prerequisites:
            indegrees[pair[0]] += 1


        ## Q: # classes can take
        ## counter: # classes have taken
        Q = []
        counter = 0
        for i in range(numCourses):
            if (indegrees[i]) == 0:
                Q.append(i)


        while Q:
            element = Q.pop(-1)
            counter += 1

            for i in adict[element]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    Q.append(i)

        return counter == numCourses
