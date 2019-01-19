def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


sum = 0
for i in range(2, 2000001):
    if is_prime(i):
        sum += i

print(sum)
