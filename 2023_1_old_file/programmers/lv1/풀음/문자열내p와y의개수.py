def solution(s):
    a, b = s.count("p") , s.count("y")
    a += s.count("P");  b += s.count("Y")
    if a == b:
        return True
    return False
