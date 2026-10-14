class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0]*numCourses
        order=[]
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            state[course]=2
            order.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order[::-1]
