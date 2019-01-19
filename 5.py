def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


ans = 1
for i in range(1, 20):
    t = i
    t /= gcd(ans, i)
    ans *= t

print(ans)
