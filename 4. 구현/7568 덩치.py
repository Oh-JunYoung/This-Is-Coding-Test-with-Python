def solution(n, people):
    answer = []
    for source in people:
        k = 1
        for target in people:
            if(source[0] < target[0] and source[1] < target[1]):
                k += 1

        answer.append(k)

    return answer

n = int(input())

people = []
for _ in range(n):
    people.append(list(map(int, input().split(" "))))

answer = solution(n, people)

for i in answer:
    print(i, end = " ")