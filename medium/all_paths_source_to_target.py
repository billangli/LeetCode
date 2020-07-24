class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        def dfs(node: int, curr_path: List[int], end: int) -> None:
            curr_path.append(node)
            if node == end:
                result.append([x for x in curr_path])
            for child in graph[node]:
                dfs(child, curr_path, end)
            curr_path.remove(node)
            
        dfs(0, [], len(graph) - 1)
        return result
