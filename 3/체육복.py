def solution(n, lost, reserve):
    ## 가지고 있는 체육복 수
    having = [1 for _ in range(n + 2)]

    ## 도난 당한 학생
    for i in lost:
        having[i] -= 1

    ## 여분이 있는 학생
    for i in reserve:
        having[i] += 1

    ## 체육복이 없는 애는 먼저 앞에 애한테 빌리고 뒤에 애한테 빌린다.
    for i in range(1, n + 1):
        if (having[i] == 0 and having[i - 1] == 2):
            having[i] += 1
            having[i - 1] -= 1

        if (having[i] == 0 and having[i + 1] == 2):
            having[i] += 1
            having[i + 1] -= 1

    ## 체육복을 갖고 있는 사람 구하기 (0번과 n + 1번 친구는 없다.)
    answer = -2
    for i in having:
        if (i >= 1):
            answer += 1

    return answer