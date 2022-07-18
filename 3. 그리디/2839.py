import sys

def solution(n):
    ## 5 킬로그램으로 꽉 채울 때 봉지 수
    cnt_5 = n // 5 + 1

    ## 3 킬로그램으로 꽉 채울 때 봉지 수
    cnt_3 = n // 3 + 1

    result = sys.maxsize

    ## 5킬로그램 부터 채우고 나서 3킬로그램으로 채운다. (강력한 알고리즘)
    # O(n ^ 2)
    for x in range(cnt_5):
        for y in range(cnt_3):
            
            ## 5 킬로그램으로 채우고 3 킬로그램으로 채웠을 때 무게
            current = x * 5 + y * 3
            
            ## 만약 정확하게 n 이라면, 최대한 적은 봉지의 개수
            if(current == n):
                result = min(result, x + y)

    return result

## 입력 : N 킬로그램
n = int(input())

## 정답 출력
result = solution(n)

## 만약 정확하게 n 을 채우지 못했다면
if(result == sys.maxsize):
    print(-1)

else:
    print(result)