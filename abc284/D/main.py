#!/usr/bin/env python3
from collections import defaultdict
from math import gcd

class PollardsRho():
    def __init__(self) -> None:
        pass

    def _isprime(self, n: int):
        if n < 2:
            return False
        i = 2
        while i * i <= n: # sqrt(N)まで試し割りする。
            if n % i == 0:
                return False
            i += 1
        return True

    # 疑似乱数生成
    def _get_rand(self, n, mod: int, seed: int):
        return (pow(n, 2, mod) + seed) % mod

    def _get_prime_recursive(self, target, N: int, _seed = 3):
        if self._isprime(target):
            return target
        x, y, g = 2, 2, 1
        seed = _seed
        while g == 1:
            x = self._get_rand(x, N, seed)
            y = self._get_rand(self._get_rand(y, N, seed), N, seed)
            g = gcd(abs(x - y), target)
            seed += 1

        if g % 2 == 0: return 2 # 最大公約数が偶数なら2
        return self._get_prime_recursive(g, N, 1) if self._isprime(g) else self._get_prime_recursive(g, N, 1)

    # メイン
    def factorization(self, N: int):
        dic = defaultdict(int)
        rest = N

        if(self._isprime(rest)):
            dic[rest] = 1
            return dic

        while True:
            ret = self._get_prime_recursive(rest, N)
            dic[ret] += 1
            rest //= ret
            if rest == 1 or rest // ret == 0:
                break

        return dic

def main():
    T = int(input())
    p = PollardsRho()
    for _ in range(T):
        N = int(input())
        print(p.factorization(N))


        

if __name__ == '__main__':
    main()
