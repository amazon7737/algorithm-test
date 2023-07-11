def solution(dots):
    dots.sort();a = max(dots);b = min(dots)
    return (a[0]-b[0])*(a[1]-b[1])
