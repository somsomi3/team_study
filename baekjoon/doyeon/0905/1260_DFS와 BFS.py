def dfs(c):
    ans_dfs.append(c)
    # 방문 노드 추가
    v[c] = 1

    for n in lst[c]:
        # 방문하지 않은 경우
        if v[n] == 0:
            dfs(n)

def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in lst[c]:
            if v[n] == 0:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


N,M,V = map(int,input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    N1,N2 = map(int,input().split())
    lst[N1].append(N2)
    lst[N2].append(N1)

for i in range(1,N+1):
    lst[i].sort()

# DFS
v = [0]*(N+1)
ans_dfs = []
dfs(V)

#BFS
v = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)