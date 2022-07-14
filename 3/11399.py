def solution(n, p):
    ## 시간이 짧은 사람부터 줄을 선다. -> O(n log n)
    p.sort()

    ## 사람들의 필요한 시간을 저장하기
    people_time = [0 for _ in range(n)]

    ## 필요한 시간 = 대기 시간 + 시간 -> O(n)
    people_time[0] = p[0]
    for i in range(1, n):
        people_time[i] = people_time[i - 1] + p[i]

    ## 총 필요한 시간
    return sum(people_time)

## 첫번째 줄 : 사람의 수
## 두번째 줄 : 걸리는 시간
n = int(input())
p = list(map(int, input().split(" ")))

## 정답 출력
print(solution(n, p))