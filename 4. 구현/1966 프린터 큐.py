import heapq
from collections import deque

def solution(n, loc, priority):
    ## index와 함께 있는 리스트를 만든다.
    priorityList = []
    for index, p in enumerate(priority):
        priorityList.append((-p, index))

    ## 우선 순위 큐를 만든다.
    priorityQ = priorityList.copy()
    heapq.heapify(priorityQ)

    ## 큐를 만든다.
    q = deque(priorityList.copy())

    ## 프린트 되는 순서와 저장할 리스트를 만든다.
    turn = 1
    answer = [0 for _ in range(n)]

    ## 모든 프린트의 순서를 구한다.
    while(len(priorityQ)):
        ## 가장 높은 우선순위를 찾고
        p, index = heapq.heappop(priorityQ)

        while(True):
            ## 가장 높은 우선순위를 가진 프린트를 찾는다.
            nextP, nextIndex = q.popleft()

            ## 프린트를 찾으면 프린트하고
            if(p == nextP):
                answer[nextIndex] = turn
                break
            
            ## 프린트가 아니면 맨 뒤로 옮긴다.
            q.append((nextP, nextIndex))
        
        ## 순서를 증가한다.
        turn += 1

    ## loc의 프린트의 순서를 출력한다.
    return answer[loc]

t = int(input())

for _ in range(t):
    n, loc = list(map(int, input().split(" ")))

    priority = list(map(int, input().split(" ")))

    answer = solution(n, loc, priority)
    print(answer)