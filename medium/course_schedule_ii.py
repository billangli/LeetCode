class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def visit(node: int) -> bool:
            if node in perm_mark:
                return True
            if node in temp_mark:
                return False
            temp_mark.add(node)
            
            for p in prereqs[node]:
                if not visit(p):
                    return False
                
            temp_mark.remove(node)
            perm_mark.add(node)
            ordering.append(node)
            return True
            
        no_mark = set()
        temp_mark = set()
        perm_mark = set()
        for i in range(numCourses):
            no_mark.add(i)
            
        prereqs = defaultdict(list)
        for p in prerequisites:
            prereqs[p[0]].append(p[1])
            # if p[1] in no_mark:
            #     no_mark.remove(p[1])
        ordering = []
        
        while len(no_mark) > 0:
            n = no_mark.pop()
            if not visit(n):
                return []
        
        return ordering
