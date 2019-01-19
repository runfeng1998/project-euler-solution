for i in range(1, 1000):
    for j in range(i, 1000):
        if i + j >= 1000:
            continue
        k = 1000 - i - j
        if k < j:
            continue
        if i * i + j * j == k * k:
            print(i, j, k)
            print(i*j*k)
