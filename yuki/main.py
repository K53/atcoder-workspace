#!/usr/bin/env python3
import sys

class Eratosthenes():
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
    
    def getPrimes(self):
        return self.primes
    
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

def main():
    N = int(input())
    A = list(map(int, input().split()))
    er = Eratosthenes(10 ** 6 + 1)
    pf = []
    for aa in A:
        s = 0
        for _, exp in er.factorize(aa):
            s += exp
        pf.append(s)
    ans = 0
    for i in pf:
        ans ^= i
    print("white" if ans else "black")
    return

if __name__ == '__main__':
    main()