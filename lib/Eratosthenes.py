# ------------------------------------------------------------------------------
#     * エラトステネスの篩
#     * 高速素因数分解
#     * 高速約数列挙
# ------------------------------------------------------------------------------
# 解説
# - 1. エラトステネスの篩 (N以下の素数列挙)
# Nまでの素数と判定されている数pでその倍数を排除していき、残った数を素数とする。
# 
# - 2. 高速素因数分解 (1 ~ N の全ての数を素因数分解するアルゴリズム)
# 1で素数リストの生成を応用して要素iの最小素因数を配列minfactorに格納する。
# minfactor[i]はiの最小の素因数であることから、iを割れるだけ割る。
# 余りをjとする時、同様にminfactor[j]はjの最小の素因数であることから、割れるだけ割る・・・
# これを繰り返すことで、全ての素因数を抽出することができる。
# 
# - 3. 高速約数列挙
# 2で素因数のリストを取得し、その組み合わせで表現できる約数を全列挙する。
# 
# リンク
# - https://qiita.com/drken/items/3beb679e54266f20ab63
# 
# 計算量
# - 1. エラトステネスの篩
#   - O(NloglogN)
# - 2. 高速素因数分解
#  - O(NlogN)   ・・・厳密にはO(NloglogN + NlogN)
# - 3. 高速約数列挙
#  - O(σ(N))
#  - 注) σ(N) : 数Nの約数の数
# 
# verify
# - https://yukicoder.me/problems/no/1665
# - https://atcoder.jp/contests/abc179/tasks/abc179_c
# - https://yukicoder.me/problems/no/713
# ------------------------------------------------------------------------------
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

# Usage
N = 12
er = Eratosthenes(N)
print(er.primes)
"-> [2, 3, 5, 7, 11]"

M = 10 ** 5
er = Eratosthenes(M)
print(er.factorize(120))
"-> [(2, 3), (3, 1), (5, 1)]"
# 120 = 2^3 + 3^1 + 5^1

M = 10 ** 5
er = Eratosthenes(M)
print(er.getDivisors(120))
"-> [1, 2, 4, 8, 3, 6, 12, 24, 5, 10, 20, 40, 15, 30, 60, 120]"