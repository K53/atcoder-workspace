#!/usr/bin/env python3
import sys

class Eratosthenes():
    """ 素数列挙
    計算量 : O(NloglogN)
    """
    def __init__(self, N: int) -> None:
        self.primeTable = [True] * (N + 1) # 数iが素数かどうかのフラグ
        self.primeTable[0] = False
        self.primeTable[1] = False
        self.minfactor = [0] * (N + 1) # 数iの最小の素因数
        self.minfactor[1] = 1
        self.primes = []    # 数Nまでの素数のリスト
        for p in range(2, N + 1):  # p : 判定対象の数
            if not self.primeTable[p]:
                continue
            self.minfactor[p] = p
            self.primes.append(p)
            # pが素数のためそれ以降に出現するpの倍数を除外する。
            # なお、ループはp始まりでも良いが、p * _ のかける側はすでに同じ処理で弾かれているはずのため無駄。
            for i in range(p * p, N + 1, p):
                if self.minfactor[i] == 0:
                    self.minfactor[i] = p
                self.primeTable[i] = False
        return
    
    """ 素数判定
    計算量 : 0(1)
    """
    def isPrime(self, n: int) -> bool:
        return self.primeTable[n]

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

def solve(A: int, B: int, C: int, D: int):
    er = Eratosthenes(200)
    s = set(er.primes)
    for i in range(A, B + 1):
        for j in range(C, D + 1):
            if i + j in s:
                break
        else:
            print("Takahashi")
            return
    print("Aoki")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)

if __name__ == '__main__':
    main()
