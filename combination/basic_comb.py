# 5C3

arr = [1,2,3,4,5]
# r: 뽑을 개수, c: 현재 인덱스
def combinations(r, new_arr, c):

    if len(new_arr) == r: # 다 뽑으면 return
        print(new_arr)
        return

    for i in range(c, len(arr)):
        combinations(r, new_arr + [arr[i]], c+1)

combinations(2, [], 0)