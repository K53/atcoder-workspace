for p in range(20):
    print(bin(p))
    print(p, ":", p&-p)
    print(p, ":", p - (p&-p) // 2)