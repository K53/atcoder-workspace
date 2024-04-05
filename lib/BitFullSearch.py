N = 8
# 2^N 通りのビット全探索。
for n in range(2 ** N):
    for i in range(N):
        if (n >> i) & 1:
            # i桁目のビットが立っている場合の処理
            pass

# 3進数などの場合
for i in range(3 ** N):
    p = i
    for b in range(N):
        p, q = divmod(p, 3)
        if q == 0: # b桁目が0の場合の処理
            pass
        elif q == 1: # b桁目が1の場合の処理
            pass
        else:
            pass
# → 仕組みN進数変換のコード参照
        

# bのNビット目を0にする。
# https://yottagin.com/?p=5139
def unset_nth_bit(b: int, N: int):
    return b & ~(1 << N)

def set_nth_bit(b: int, N: int):
    return b | (1 << N)