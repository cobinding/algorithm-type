arr = [[1,2,3,4,5], [6,7,8,9,10]]
# m = 가로 = 열의 움직임 = 안쪽 포문
n, m = len(arr), len(arr[0])

# 직사각형 90도 회전
# 90도 회전은 가로, 세로 뒤바뀜 !
new_90 = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m): # m = 5 = 세로
        new_90[j][n-i-1] = arr[i][j]

print(new_90)

# 직사각형 180도 회전
# 180도는 가로, 세로 그대로에 인덱스만 reverse
new_180 = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        new_180[n-i-1][m-j-1] = arr[i][j]

print(new_180)

# 직사각형 270도 회전
# 270도는 가로, 세로 바뀜
new_270 = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        new_270[m-j-1][i] = arr[i][j]

print(new_270)