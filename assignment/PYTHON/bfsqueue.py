def bfs(graph,start):
    visited = set()
    s = [start]     
    visited.add(start)
    while s:
        node = s.pop(0)    
        print(node,end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                s.append(neighbor)
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}
bfs(graph,0)