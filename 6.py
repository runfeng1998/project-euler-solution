Sum = 0
Sum2 = 0

for i in range(1, 101):
    Sum += i
    Sum2 += i * i

print(Sum, Sum2)
print(Sum * Sum - Sum2)
