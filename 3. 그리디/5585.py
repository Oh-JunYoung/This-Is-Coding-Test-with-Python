def solution(n):
    ## 잡화점이 갖고 있는 동전
    coin = [1, 5, 10, 50, 100, 500]

    ## 금액이 큰 동전으로 거슬러 주기 위한 정렬
    coin.sort()

    ## 거스름 돈
    remain = 1000 - n
    
    ## 전체 동전의 개수
    total_cnt = 0
    
    ## 거슬러줄 동전 : O(6)
    ## 가장 큰 금액부터 거슬러 주기 (핵심 알고리즘)
    while(len(coin)):
        ## 금액이 가장 큰 동전부터 꺼내기
        current_coin = coin.pop()
        
        ## 현재 거슬러줄 동전의 개수 구하기
        current_cnt = remain // current_coin

        ## 거슬러줄 남은 금액
        remain -= (current_coin * current_cnt)
        
        ## 전체 동전의 개수 구하기
        total_cnt += current_cnt

    return total_cnt


## 입력 : 물건의 금액
n = int(input())

## 정답 출력
print(solution(n))