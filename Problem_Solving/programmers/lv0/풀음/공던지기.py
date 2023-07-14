def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1
# k번째로 던져진 지점이 아니라 던진 사람이기 때문에 k - 1을 해주고, 한 사람씩 건너뛰므로 2를 곱해준 값을 배열의 크기로 나눈 index의 숫자가 답.
