# 삼성전자 SW 역량테스트 빈출코드 정리 !

# --- 정사각형 90, 180, 270 시계/반시계 회전 --- #

arr = [[1,2,3], [4,5,6], [7,8,9]]
n = 3

# 시계 90 & 반시계 270 회전
new_90 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_90[j][n-i-1] = arr[i][j]

# 시계 180 & 반시계 180 회전
new_180 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n-i-1][n-j-1] = arr[i][j]

# 시계 270 & 반시계 90
new_270 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_270[n-1-j][i] = arr[i][j]

