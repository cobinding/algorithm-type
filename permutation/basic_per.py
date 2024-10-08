
n = int(input().rstrip())
visited = [False] * (n+1)
answer = []

# 중복없는 순열
def permutations(curr_num):
    if curr_num == n+1 :
        print(answer)
        return

    # 1부터 n까지 순열을 만드는 과정
    for i in range(1, n+1):
        if visited[i] :
            continue

        # 사용한 숫자에 대한 방문 처리
        visited[i] = True
        answer.append(i)
        print("append, ", answer, visited )
        # 순서 보장을 위해 자릿수 1씩 늘려가면서 함수 호출
        permutations(curr_num+1)

        # 조건에 해당할 때까지 append 수행
        # return 조건에 다다르면 호출된 재귀스택들이 return 하면서 pop
        # 방문 처리 && 숫자 만들기까지 끝내고 return 됨 -> 백트래킹 특징(구하려는 해가 아닐 것같으면 손절)
        answer.pop()
        print("pop", answer, visited)
        visited[i] = False

# permutations(1)