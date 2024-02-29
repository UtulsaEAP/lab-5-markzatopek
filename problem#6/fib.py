def fibonacci(n):
    if n < 0: return -1
    a = 0
    b = 0
    for _ in range(n):
        a += b
        b = a - b
        if a == 0: a = 1
    return a


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')