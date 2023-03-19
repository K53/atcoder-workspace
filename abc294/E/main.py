#!/usr/bin/env python3
from collections import defaultdict

def main():
    L, N1, N2 = map(int, input().split())
    d = defaultdict(list) #(l, r) rを含まない
    cur = 0
    for i in range(N1):
        v, l = map(int, input().split())
        d[v].append((cur, cur + l))
        cur += l
    cur = 0
    for i in range(N2):
        v, l = map(int, input().split())
        d[v].append((cur, cur + l))
        cur += l
    # print(d)
    ans = 0

    for val, pair in d.items():
        s = set()
        for l, r in pair:
            s.add(l)
            s.add(r)
        # 圧縮
        raw_to_compressed = {}
        compressed_to_raw = []
        for index, val in enumerate(sorted(list(s))):
            raw_to_compressed[val] = index
            compressed_to_raw.append(val)

        # テーブルの初期化
        imos = [0] * len(compressed_to_raw)
        for l, r in pair:
            imos[raw_to_compressed[l]] += 1
            imos[raw_to_compressed[r]] -= 1
                
        # ビルド
        for i in range(1, len(imos)):
            imos[i] += imos[i - 1]
        
        # print(imos)
        for i in range(len(compressed_to_raw) - 1):
            if imos[i] == 2:
                # value_on_imos = imos[i] # imosテーブル上の値
                # print(compressed_to_raw[i + 1], compressed_to_raw[i])
                span = compressed_to_raw[i + 1] - compressed_to_raw[i] # その値をとり続ける実際の値の長さ
                ans += span
    print(ans)

if __name__ == '__main__':
    main()
