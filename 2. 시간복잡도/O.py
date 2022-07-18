n = 1000

## 1. O(1)

O_n = 0
l = list()
l.append(1) ## (= push)
l.pop()
O_n += 1
print(f"O(1) :\t\t{O_n}")

## 2. O(log n)

O_n = 0
for i in range(0, n, 100):    ## 100개 씩 건너 뛰는 것에 주목
    O_n += 1
print(f"O(log n) :\t{O_n}")

## 3. O(n)
O_n = 0
for i in range(0, n):
    O_n += 1
print(f"O(n) :\t\t{O_n}")


## 4. O(n * log n)
O_n = 0
for i in range(0, n, 100):    ## 100개 씩 건너 뛰는 것에 주목
    for j in range(0, n):
        O_n += 1
print(f"O(n * log n) :\t{O_n}")


## 5. O(n^2)
O_n = 0
for i in range(0, n):
    for j in range(0, n):
        O_n += 1
print(f"O(n^2) :\t{O_n}")


## 6. O(n^3)
n = 10
O_n = 0
for i in range(0, n):
    for j in range(0, n):
        for z in range(0, n):
            O_n += 1
print(f"O(n^3) :\t{O_n} \t info : O(n^3)은 10억 이상이다. 10억 이상 넘어가는 연산은 매우 부적절하다. n을 10로 수정")

## 7. O(2^n)

n = 5
O_n = 1
def pibo(x):
    global O_n

    O_n += 1

    if(x == 0):
        return 0

    if(x == 1):
        return 1

    return pibo(x - 1) + pibo(x - 2)

pibo(n)

print(f"O(2^n) :\t{O_n} \t info : O(2^n)은 2 ^ 1000 이상이다. 연산이 너무 커서 CPU가 연산을 하려면 평생을 해야한다. n을 5로 수정")
