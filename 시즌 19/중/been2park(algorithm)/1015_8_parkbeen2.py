from collections import deque

M, N, H = map(int, input().split())

tomato = []
queue = deque()

for h in range(H):
    box = []
    for n in range(N):
        row = list(map(int, input().split()))
        box.append(row)

        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m))

    tomato.append(box)

# 위, 아래, 앞, 뒤, 왼쪽, 오른쪽
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]

# BFS
while queue:
    h, n, m = queue.popleft()

    for i in range(6):
        nh = h + dh[i]
        nn = n + dn[i]
        nm = m + dm[i]

        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if tomato[nh][nn][nm] == 0:
                tomato[nh][nn][nm] = tomato[h][n][m] + 1
                queue.append((nh, nn, nm))

# 결과 확인
answer = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:
                print(-1)
                exit()

            answer = max(answer, tomato[h][n][m])

print(answer - 1)
