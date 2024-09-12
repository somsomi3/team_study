from collections import deque  # BFS에서 사용할 deque를 가져옴

# DFS 함수 정의 (깊이 우선 탐색)
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')  # 방문한 노드 출력
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in sorted(graph[v]):  # 번호가 작은 것부터 방문하기 위해 정렬
        if not visited[i]:  # 아직 방문하지 않았다면
            dfs(graph, i, visited)  # 재귀 호출로 방문

# BFS 함수 정의 (너비 우선 탐색)
def bfs(graph, start, visited):
    queue = deque([start])  # 큐에 시작 노드를 넣음
    visited[start] = True  # 시작 노드를 방문 처리
    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 하나의 원소를 꺼냄
        print(v, end=' ')  # 방문한 노드 출력
        # 현재 노드와 연결된 다른 노드들을 큐에 넣음
        for i in sorted(graph[v]):  # 번호가 작은 것부터 방문하기 위해 정렬
            if not visited[i]:  # 아직 방문하지 않았다면
                queue.append(i)  # 큐에 추가
                visited[i] = True  # 방문 처리

# 입력 받기
n, m, v = map(int, input().split())  # 정점 개수, 간선 개수, 시작 정점 입력
graph = [[] for _ in range(n + 1)]  # 인접 리스트로 그래프 초기화

# 그래프 입력 (간선 정보)
for _ in range(m):
    a, b = map(int, input().split())  # 간선 정보 입력
    graph[a].append(b)  # 양방향이므로 두 노드 모두 추가
    graph[b].append(a)

# DFS 실행
visited = [False] * (n + 1)  # 방문 기록을 위한 리스트 초기화
dfs(graph, v, visited)  # DFS 탐색 시작
print()  # DFS 결과 출력 후 줄바꿈

# BFS 실행
visited = [False] * (n + 1)  # 방문 기록 리스트 재초기화
bfs(graph, v, visited)  # BFS 탐색 시작
