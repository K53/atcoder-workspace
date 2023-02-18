def solve(s, gx, gy):
    s = list(map(len, s.split("T")))
    x, y = {s[0]}, {0}
    for dx in s[2::2]:
        tmp = set()
        for i in x:
            tmp.add(i + dx)
            tmp.add(i - dx)
        x = tmp
    for dy in s[1::2]:
        tmp = set()
        for i in y:
            tmp.add(i + dy)
            tmp.add(i - dy)
        y = tmp

    if gx in x and gy in y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
