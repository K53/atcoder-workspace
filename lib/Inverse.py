# ------------------------------------------------------------------------------
#     法をPとした時(mod P条件下)のAの逆元A^-1算出
# ------------------------------------------------------------------------------
#
# ■ case1 - Pが素数の場合(この場合、必然的にAとPは互いに素)、
#  フェルマーの小定理から、
#   ---------------------------------
#   A^-1 ≡ A^(P-2) (mod P) が成立する。
#   ---------------------------------
# なお、複数のA^-1を必要とする場合、
#  getInverses()から1〜Nまでのmod Pにおける逆元のリストをO(N)で算出できる。 
#   ---------------------------------
#   L ≡ getInverses(N, P)
#   ---------------------------------
#   計算量: O(N)
#
# ■ case2 - AとPが互いに素の場合、
#  拡張ユークリッドの互除法から算出。
#   ---------------------------------
#   A^-1 ≡ ext_gcd(A, P) 
#   ---------------------------------
#   計算量: O(log(max(A, P)))
#
#  - 解説
#     a * x + MOD * y = 1 を満たす(x, y)があるとして、両辺を法をMODとして割るとを取ると、
#     a * x ≡ 1 (mod MOD) となることから、このxはMOD下のaの逆元といえる。 
#
# 参考
# - https://gist.github.com/catupper/cb9a146dd21a9916e75deef90991169d
# - https://www.youtube.com/watch?v=eiJyDb9c3Js
# ------------------------------------------------------------------------------

# 1 〜 N の逆元列挙
def getInverses(N: int, mod: int):
    """
    法modにおける 1 〜 N の逆元列挙
    O(N)
    """
    inv = [0] * N
    inv[1] = 1
    for i in range(2, N):
        inv[i] = mod // i * -inv[mod % i]
        print(inv[i])
        if inv[i] < 0: inv[i] += mod
    return inv

print(getInverses(10, 100))


# 拡張ユークリッドの互除法
# ax + by = gcd(a, b) を満たす整数(a,b)の組を求める。
def ext_gcd(a: int, b: int):
    if a == 0: return (0, 1, b)
    else:
        (X, Y, g) = ext_gcd(b % a, a)
        return (Y - (b // a) * X, X, g)

def getInverse(A: int, mod: int):
    x, _, g = ext_gcd(A, mod)
    if g != 1: return -1 # no inverse exists
    return x % mod

MOD = 103
a = 17
print(ext_gcd(a, MOD))



