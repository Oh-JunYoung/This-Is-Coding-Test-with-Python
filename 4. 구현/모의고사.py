def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    correct = [0, 0, 0, 0]
    
    for index, a in enumerate(answers):
        if(s1[index % len(s1)] == a):
            correct[1] += 1
            
        if(s2[index % len(s2)] == a):
            correct[2] += 1
            
        if(s3[index % len(s3)] == a):
            correct[3] += 1
        
    answer = []
    maxV = max(correct)
    
    for index, c in enumerate(correct):
        if(c == maxV):
            answer.append(index)
    
    return answer