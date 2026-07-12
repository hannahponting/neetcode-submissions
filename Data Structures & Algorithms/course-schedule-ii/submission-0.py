class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        def dfs(course):
            if preMap[course] == []:
                if course not in res:
                    res.append(course)
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            if course not in res:
                res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res