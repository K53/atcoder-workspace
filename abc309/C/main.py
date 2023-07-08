#!/usr/bin/env python3
import sys


def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    # 圧縮
    s = set([1])
    s |= set([aa + 1 for aa in a])
    raw_to_compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(s))):
        raw_to_compressed[val] = index
        compressed_to_raw.append(val)

    # テーブルの初期化
    imos = [0] * len(compressed_to_raw)
    for i in range(N):
        imos[raw_to_compressed[1]] += b[i]
        imos[raw_to_compressed[a[i] + 1]] -= b[i]
        
    # ビルド
    for i in range(1, len(imos)):
        imos[i] += imos[i - 1]
    
    # print(imos)

    for i in range(len(imos)):
        if imos[i] <= K:
            print(compressed_to_raw[i])
            return

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)

if __name__ == '__main__':
    main()
