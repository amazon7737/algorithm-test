def solution(strings, n):
    # lambda
    return sorted(strings, key=lambda x: (x[n], x))
