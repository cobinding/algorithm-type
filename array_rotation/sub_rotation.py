# 전체 배열이 아닌 특정 부분만 배열시키는 것

# 전체 7*7 배열
arr = [[7 * j + i for i in range(1,8)] for j in range(7)]
new_arr = [[0]*7 for _ in range(7)]

sy, sx = 2, 2 # 회전하고자 하는 위치 좌표
length = 3 # l*l만큼 회전

# sy = y값 = 세로 = 행
# sx = x값 = 가로 = 열
def rotation(sy, sx, n):
    global arr, new_arr

    for y in range(sy, sy+n):
        for x in range(sx, sx+n):
            # 1. 모두 0으로 만들어주기
            oy, ox = y-sy, x-sx

            # 2. 90도 회전 만들기
            ry, rx = ox, length-oy-1

            # 3. ry+sy 하기
            new_arr[sy+ry][sx+rx] = arr[y][x]


    for y in range(sy, sy+n):
        for x in range(sx, sx+n):
            arr[y][x] = new_arr[y][x]

rotation(sy, sx, length)
for item in arr:
    print(item)