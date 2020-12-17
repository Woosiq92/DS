# 1. DFS : 깊이 우선 탐색 ( 깊은 부분 우선 )
# 인접리스트 방식 : 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장 (파이썬은 인접행렬을 리스트로 구현) 
# 인접 리스트는 연결된 정보만을 저장하여 메모리를 효율적으로 사용 
# 그러나 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. ( 연결된 데이터를 하나씩 확인해야 하기 때문) 

# 동작 과정 ( 스택 사용 ) 
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다. 
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.  
# 3. 1,2 번 과정을 더 이상 수행할 수 없을 때까지 반복한다. 

# 방문 처리 : 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것, 각 노드를 한 번씩만 처리할 수 있다.

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 ( 2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


# 각 노드가 방문된 정보를 리스트 자료형으로 표현 ( 1차원 리스트 )
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

#BFS

from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프 정의
# 각 노드가 방문된 정보를 리스트 자료형으로 표현 ( 1차원 리스트 )
# 정의된 DFS 함수 호출