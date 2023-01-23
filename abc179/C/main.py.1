#!/usr/bin/env python3
import sys
import math

class Eratosthenes():
    """ 素数列挙
    計算量 : O(NloglogN)
    """
    def __init__(self, N: int) -> None:
        self.isPrime = [True] * (N + 1) # 数iが素数かどうかのフラグ
        self.isPrime[0] = False
        self.isPrime[1] = False
        self.minfactor = [0] * (N + 1) # 数iの最小の素因数
        self.minfactor[1] = 1
        self.primes = []    # 数Nまでの素数のリスト
        for p in range(2, N + 1):  # p : 判定対象の数
            if not self.isPrime[p]:
                continue
            self.minfactor[p] = p
            self.primes.append(p)
            # pが素数のためそれ以降に出現するpの倍数を除外する。
            # なお、ループはp始まりでも良いが、p * _ のかける側はすでに同じ処理で弾かれているはずのため無駄。
            for i in range(p * p, N + 1, p):
                if self.minfactor[i] == 0:
                    self.minfactor[i] = p
                self.isPrime[i] = False
        return
    
    """ 高速素因数分解
    計算量 : O(NlogN)
    """
    def factorize(self, n: int) -> list:
        res = [] # (p, exp)
        while n > 1:
            p = self.minfactor[n]
            exp = 0
            while self.minfactor[n] == p:
                n //= p
                exp += 1
            res.append((p, exp))
        return res

    """ 高速約数列挙
    計算量 : O(σ(N)) 
    注) σ(N) : 数Nの約数の数
    """
    def getDivisors(self, n: int) -> list:
        res = [1]
        for p in self.factorize(n):
            for i in range(len(res)):
                v = 1
                for _ in range(p[1]):
                    v *= p[0]
                    res.append(res[i] * v)
        return res

def main():
    N = int(input())
    er = Eratosthenes(N)
    ans = 0
    for ab in range(1, N):
        ans += len(er.getDivisors(ab))
    print(ans)
    return


if __name__ == '__main__':
    main()
