import  gmpy2
sum = 1

for i in range(1, 101):
    sum = sum * i

ans = 0
while sum > 0:
    ans += sum % 10
    sum /= 10

print(sum)
print(ans)
