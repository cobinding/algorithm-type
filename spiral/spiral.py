from calendar import month

arr = [[0]*5 for _ in range(5)]

def spiral():
    global arr
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y = len(arr)//2, len(arr)//2

    # 필요한 거 4가지
    d_idx = 0
    dist = 1 # 현재 이동 범위
    num = 0 # 넣어줄 숫자
    move_cnt = 0


    while True:
        for _ in range(dist):
            dy,dx = d[d_idx]

            ny, nx = dy+y, dx+x
            if (ny,nx) == (0,-1):
                return

            num += 1; arr[ny][nx] = num

            y, x = ny, nx


        # 방향과 움직임 체크 !!
        if move_cnt == 2:
            move_cnt = 0
            d_idx = (d_idx+1) % 4

