def solution(a, b):
    t1 = min(a, b)
    t2 = max(a, b)
    sum = 0
    for i in range(t1, t2 + 1):
        sum += i
    return sum