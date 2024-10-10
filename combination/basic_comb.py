
# 조합 - 순서 상관없고 중복 불가
# 1,2,3 == 3,2,1 이기 때문에 이전에 방문했던 곳은 재방문 X
# 탐색범위는 나부터 끝까지 (내 앞은 안 봄)

arr = [1,2,3,4,5]
r = 3
comb = []

def combination(start, curr_num):
    if curr_num == r:
        print(comb)
        return

    # 나부터 끝까지 탐색
    for i in range(start, len(arr)):
        comb.append(arr[i])
        combination(i+1, curr_num+1)
        comb.pop()

combination(0,0)