from collections import deque

def solution(n, wordList):
    answer = 0

    for word in wordList: ## O(n)
        wordSet = set()
        isGroupWord = True

        word = deque(word)
        while(len(word)): ## O(n)
            ## 단어의 앞에서 부터 하나씩 꺼내서
            currentAlpha = word.popleft()

            ## 이미 전에 있었던 단어면 그룹 단어가 아니다.
            if(currentAlpha in wordSet):
                isGroupWord = False
                break
            
            ## 알파벳을 set에 넣는다.
            wordSet.add(currentAlpha)

            ## 다른 알파벳이 나올 때 까지 꺼내버린다.
            while(len(word)):
                nextAlpha = word.popleft()
                if(currentAlpha != nextAlpha):
                    word.appendleft(nextAlpha)
                    break


        if(isGroupWord):
            answer += 1
        
    return answer

n = int(input())

wordList = []
for _ in range(n):
    wordList.append(input())

print(solution(n, wordList))
