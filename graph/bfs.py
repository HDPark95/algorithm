#너비 우선 탐색 알고리즘인 BFS는 큐자료구조에 기초한다는 점에서 구현이 간단하며, 파이선에서는 deque 라이브러리를 사용하는 것이 좋다.

from collections import deque

def bfs(graph, start, visited):
    #큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
