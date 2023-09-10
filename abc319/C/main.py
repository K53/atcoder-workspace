#!/usr/bin/env python3
from itertools import permutations

def main():
    C = []
    count = 0
    for _ in range(3):
        C.append(list(map(int, input().split())))
    # for per in [[6,3,0,1,2,4,5,7,8]]:#permutations(range(9)):
    for per in permutations(range(9)):
        l = [[] for _ in range(8)]
        check = list(range(8))
        for i in per:
            p, q = divmod(i, 3)
            num = C[p][q]
            if i == 0:
                l[0].append(num)
                l[3].append(num)
                l[6].append(num)
            elif i == 1:
                l[0].append(num)
                l[4].append(num)
            elif i == 2:
                l[0].append(num)
                l[5].append(num)
                l[7].append(num)
            elif i == 3:
                l[1].append(num)
                l[3].append(num)
            elif i == 4:
                l[1].append(num)
                l[4].append(num)
                l[6].append(num)
                l[7].append(num)
            elif i == 5:
                l[1].append(num)
                l[5].append(num)
            elif i == 6:
                l[2].append(num)
                l[3].append(num)
                l[7].append(num)
            elif i == 7:
                l[2].append(num)
                l[4].append(num)
            elif i == 8:
                l[2].append(num)
                l[5].append(num)
                l[6].append(num)
            for i in check:
                if len(l[i]) == 3 and l[i][0] == l[i][1] and l[i][0] != l[i][2]:
                    count += 1
                    # check.remove(i)
                    break
            else:
                continue
            break
    print(1 - count / 362880)

if __name__ == '__main__':
    main()
