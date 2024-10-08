import sys; input=sys.stdin.readline

n,m = map(int, input().split())
perm = []
visited = [False for _ in range(n+1)]

def overlap_permutations(curr_num):
    if curr_num == m+1:
        print(*perm)
        return

    for i in range(1,n+1):
        if visited[i] == True:
            continue

        if visited[i-1] == True:
            perm.append(i)

        perm.append(i)
        overlap_permutations(curr_num+1)
        # 재귀가 return 될 때
        perm.pop()
        visited[i] = False

overlap_permutations(1)