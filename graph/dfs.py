#DFS 스택 자료구조에 기초한다. 실제로는 스택을 쓰지 않아도 되며 탐색을 수행함에 있어서 O(N)의 시간이 소요된다.


#DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=" ")
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)