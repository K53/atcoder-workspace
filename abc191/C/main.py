#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    # G = [
    #     ".....",
    #     ".#.#.",
    #     ".###.",
    #     ".#.#.",
    #     "....."
    # ]
    ans = 0
    for hh in range(H - 1):
        for ww in range(W - 1):
            if [G[hh][ww], G[hh + 1][ww], G[hh][ww + 1], G[hh + 1][ww + 1]].count("#") in [1, 3]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
