#!/usr/bin/env python3


def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        XYs = []
        for _ in range(a):
            x, y = map(int, input().split())
            XYs.append((x - 1, y))
        A.append(XYs)
    # print(A)
    ans = 0
    for case in range(2 ** N):
        # print(bin(case))
        people = [-1] * N
        count = 0
        conflict = False
        for i in range(N):
            t = case >> i
            if t & 1:
                count += 1
                if people[i] == -1:
                    people[i] = 1
                elif people[i] != 1:
                    conflict = True
                    break
                for x, y in A[i]:
                    if people[x] == -1:
                        people[x] = y
                    elif people[x] != y:
                        conflict = True
                        break
            else:
                if people[i] == -1:
                    people[i] = 0
                elif people[i] != 0:
                    conflict = True
                    break
        if not conflict:
            # print(bin(case))
            # print(count)
            # print(people)
            # print("#")
            ans = max(ans ,count)
    print(ans)

if __name__ == '__main__':
    main()
