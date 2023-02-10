

import math


def greedy(N: int, M, pe):
    # print(M)
    # print(pe)
    s = set()
    nums = []
    for i in range(N):
        for mm in range(M[i]):
            # print(pe[i][mm])
            nums.append(pe[i][mm][0] ** pe[i][mm][1])
    print("%", nums)
    for i in range(len(nums)):
        mul = 1
        lc = 0
        for nn in range(len(nums)):
            if nn == i:
                continue
            else:
                mul *= nums[nn]
                gc = math.gcd(lc, nums[nn])
                lc = mul // gc
                print("#", lc, i, nn)
        s.add(lc)
        return(len(s))

            
    return 

def solve(N: int, M, pe):
    # N = int(input())
    d = {} # 7: 2, set(2, 0)
    # print(d[0])
    f = 0
    for i in range(N):
        # M = int(input())
        for mm in range(M[i]):
            p, e = pe[i][mm] #map(int, input().split())
            if p in d.keys():
                if d[p][0] < e:
                    d[p] = (e, i)
                elif d[p][0] == e:
                    d[p] = (e, -1)
                else:
                    f = 1
                    continue
            else:
                d[p] = (e, i)
    # print(d)
    num = set()
    for _, idx in d.values():
        if idx == -1:
            f = 1
            continue
        num.add(idx)
    return len(num) + f

checkTimes = 10 # テスト試行回数
for i in range(checkTimes):
    import random
    N = 5
    M = []
    pe = []
    for i in range(N):
        q = random.randint(1, 3)
        M.append(q) # 発生させる乱数範囲 (末尾を含む)
        s = []
        for mm in range(q):
            prime = [2,3,5]
            index = (random.randint(1, len(prime))) - 1 # 発生させる乱数範囲 (末尾を含む)
            count = random.randint(1, 2)
            s.append((prime[index], count))
        pe.append(s)
    ac = greedy(N,M,pe)
    checkee = solve(N,M,pe)
    if ac != checkee:
        print(N,M,pe)
        print(ac, "!=", checkee)
        print("----------------")