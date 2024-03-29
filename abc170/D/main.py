#!/usr/bin/env python3
import sys
from collections import Counter
def solve(N: int, A: "List[int]"):
    l = sorted(A)
    d = Counter(A)
    primeTable = [True] * (l[-1] + 1) # 数iが素数かどうかのフラグ
    primeTable[0] = False
    minfactor = [0] * (l[-1] + 1) # 数iの最小の素因数
    minfactor[1] = 1
    primes = []    # 数Nまでの素数のリスト
    for p in l:
        if not primeTable[p]:
            continue
        minfactor[p] = p
        primes.append(p)
        # pが素数のためそれ以降に出現するpの倍数を除外する。
        # なお、ループはp始まりでも良いが、p * _ のかける側はすでに同じ処理で弾かれているはずのため無駄。
        for i in range(p * 2, l[-1] + 1, p):
            if minfactor[i] == 0:
                minfactor[i] = p
            primeTable[i] = False
    ans = 0
    for i in range(N):
        if primeTable[A[i]] and d[A[i]] == 1:
            ans += 1
    print(ans)
    return



# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
