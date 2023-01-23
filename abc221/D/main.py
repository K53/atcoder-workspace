#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    L = [aa + bb - 1 + 1 for aa, bb in zip(A, B)]
    ll = sorted(list(set(A) | set(L)))
    ll.append(max(ll) + 1)
    compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(ll):
        compressed[val] = index
        compressed_to_raw.append(val)
    # print(compressed)
    # print(compressed_to_raw)
    # テーブルの初期化
    tl = len(compressed_to_raw)
    imos = [0] * tl
    for i in range(N):
        imos[compressed[A[i]]] += 1
        imos[compressed[L[i]]] -= 1

    # ビルド
    for i in range(1, len(imos)):
        imos[i] += imos[i - 1]
    # print(imos)

    ans = [0] * (N + 1)
    for i in range(tl - 1):
        ans[imos[i]] += (compressed_to_raw[i + 1] - compressed_to_raw[i])
    print(*ans[1:])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
