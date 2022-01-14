def solution(k, a, b):
    a.sort()
    b.sort(reverse = True)
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
    answer = sum(a)
    return answer
