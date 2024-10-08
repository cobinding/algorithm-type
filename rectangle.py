'''
직사각형같은 경우는.... 가로, 세로 헷갈리지 않게 주의해야 하는데,
배열 한 덩이가 가로고
행으로 나눠진 게 세로임 
그래서 아래의 경우는 가로 = 5, 세로 = 2 
'''

arr = [[1,2,3,4,5], [6,7,8,9,10]]

# -- 시계 90 & 반시계 270 -- #
# m = 세로, n = 가로 = 5
m, n = len(arr), len(arr[0])
new_arr = [[0]*m for _ in range(n)]
# 가로 5개 세로 5가 되어야 하니까 행의 반복임
# 행의 반복은 바깥 포문
# 열의 반복은 안쪽 포문
for i in range(m):
    for j in range(n):
        new_arr[j][m-i-1] = arr[i][j]

# -- 시계 180 & 반시계 180 -- #
# * m = 가로 = 열의 움직임 = 안쪽 포문
new_180 = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        new_180[n-i-1][m-j-1] = arr[i][j]

# -- 시계 270 & 반시계 90 -- #
# m = 가로 길이 = 열의 방향 = 안쪽 포문
n, m = len(arr), len(arr[0])
new_270 = [[0]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        new_270[m-1-j][i] = arr[i]