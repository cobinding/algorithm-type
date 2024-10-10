r, c, k = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(k)]

# 1. [1]+[0]*열+[1]으로 양옆(서,동) 1로 채워주기
# 2. 젤 아래 1로 깔아주기
arr = [[1]+[0]*c+[1] for _ in range(r+3)] + [[1]*(c+2)]

#    상  우  하  좌
di = [-1, 0, 1, 0] # 행
dj = [0, 1, 0, -1] # 열
d = [(1,0),(-1,0),(0,-1),(0,1)]

# 출구
exit_set = set()

def bfs(si,sj):
    q = []
    visited = [[False]*(c+2) for _ in range(r+4)]

    q.append((si,sj))
    visited[si][sj] = True
    max_row = 0

    while q :
        ci,cj = q.pop(0)

        for dx, dy in d :
            ni, nj = ci+dx, cj+dy
            if not visited[ni][nj] and (arr[ci][cj] == arr[ni][nj] or ((ci,cj) in exit_set and arr[ni][nj] > 1)):
                q.append((ni, nj))
                visited[ni][nj] = True
                max_row = max(max_row, ni)

    return max_row - 2 # 2만큼 행을 늘려준 부분에 대해 -2





ans = 0 # 최종 행
num = 2 # 골렘 번호
for cj, dr in unit:
    ci=1 # 첫출발 행
    # 우선순위(남 > 서 > 동)에 따라 이동
    while True:
        # 1. 남쪽으로 이동 - 아래 3공간이 비었는지 확인
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0:
            ci += 1
        # 2. 서쪽으로 이동 - 좌 3공간 && 좌 이동 후 아래 2공간 비었는지 확인
        # 비어있다면 좌 & 하로 이동 & 반시계 방향으로 출구 변경
        elif arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-1] + arr[ci+1][cj-2] + arr[ci+2][cj-1] == 0:
            cj -= 1
            ci += 1
            dr = (dr-1)%4

        # 3. 서쪽으로 이동 - 우 3공간 && 우 이동 후 아래 2공간 확인
        # 비어있다면 우 & 하로 이동 & 시계 방향으로 출구 변경
        elif arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1] + arr[ci+1][cj+2] + arr[ci+2][cj+1] == 0:
            cj += 1
            ci += 1
            dr = (dr+1)%4

        # 더이상 탐색을 할 수 없는 경우
        else:
            break

    # --- [2] 골렘을 표시  --- #
    # 위 while을 돌고서, 골렘이 밖으로 튀어나온 경우 - "얘는 버리고 & 맵 reset"
    if ci<4 :
        arr = [[1] + [0] * c + [1] for _ in range(r + 3)] + [[1] * (c + 2)] # 맵 reset
        num = 2 # 골렘 number reset
        exit_set = set()
    else:
        # 1. 골렘이 돌아다닐 수 있는 경우, 골렘 영역 표시해주기
        arr[ci+1][cj]=arr[ci-1][cj]=num # 골렘 열의 좌표
        arr[ci][cj-1]=arr[ci][cj]=arr[ci][cj+1]=num
        num += 1

        # 2. 골렘 안의 정령 이동
        exit_set.add((ci+di[dr], cj+dj[dr]))
        ans += bfs(ci, cj)

print(ans)