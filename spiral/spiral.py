arr = [[0]*5 for _ in range(5)]

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 배열의 중앙 위치
y = len(arr)//2
x = len(arr)//2


def spiral():

    num = 0  # 칸에 채워넣을 값
    dist = 1 # 현재 이동 거리, 초기값 = 1
    d_idx = 0  # 현재 이동 방향의 인덱스, 초기값 = 0
    move_cnt = 0  # 현재 이동 횟ㅅ수

    while True:
        for _ in range(dist):
            # 현재 이동 방향
            dy, dx = d[d_idx]

            # 새로운 위치 계산 - (0,-1)이면 모두 돈 것이기에 종료
            ny, nx = y+dy, x+dx
            if (ny,nx) == (0,-1) :
                return

            # 칸에 1씩 늘려가면서 채워줌
            num +=1; arr[ny][nx] = num

            # 좌표 인덱스 업데이트
            y,x = ny, nx

        # 이동이 끝나면
        move_cnt += 1
        d_idx = (d_idx+1) % 4

        # 이동 횟수가 2에 도달하면 초기화
        if move_cnt == 2:
            dist += 1
            move_cnt = 0
