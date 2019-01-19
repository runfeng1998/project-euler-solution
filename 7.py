def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


cnt = 0
for i in range(1, 100000000):
    if is_prime(i):
        cnt += 1
        if cnt == 10001:
            print(i)
            exit(0)
