def dfs(x, y, n, graph, visited):
    # 스택을 사용하여 DFS 탐색을 수행
    stack = [(x, y)]
    count = 0  # 현재 단지의 집의 수
    while stack:
        cx, cy = stack.pop()  # 스택에서 좌표를 꺼냄
        if visited[cx][cy]:  # 이미 방문한 곳이면 건너뜀
            continue
        visited[cx][cy] = True  # 방문 처리
        count += 1  # 단지 내 집의 수를 증가시킴
        # 상하좌우로 이동할 좌표 계산
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            # 유효한 범위 내에서 집이 있는 경우 스택에 추가
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                stack.append((nx, ny))
    return count  # 단지의 집의 수 반환


def solve():
    n = int(input())  # 지도 크기 입력
    graph = [list(map(int, input())) for _ in range(n)]  # 지도 정보 입력 (문자열을 정수 리스트로 변환)

    visited = [[False] * n for _ in range(n)]  # 방문 여부를 기록할 배열
    complexes = []  # 각 단지의 집의 수를 저장할 리스트

    # 2차원 배열을 순회하면서 단지를 탐색
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:  # 집이 있고 방문하지 않은 경우
                size = dfs(i, j, n, graph, visited)  # DFS로 단지 크기를 계산
                complexes.append(size)  # 단지 크기를 리스트에 추가

    complexes.sort()  # 단지 크기를 오름차순으로 정렬
    print(len(complexes))  # 단지의 수 출력
    for size in complexes:  # 각 단지의 크기를 출력
        print(size)


# 백준에서 프로그램 실행 시 자동으로 입력을 받도록 main 함수처럼 사용
if __name__ == "__main__":
    solve()
