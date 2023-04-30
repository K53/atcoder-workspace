#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)
MOD = 1000000007  # type: int

def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        G[a[i] - 1].append(b[i] - 1)
        G[b[i] - 1].append(a[i] - 1)
    fixG = [[] for _ in range(N)]
    ans = K
    
    def dfs(cur, pre):
        nonlocal ans
        if pre != -1:
            fixG[pre].append(cur)
            fixG[cur].append(pre)
            fixed = len(fixG[pre])
            # print(fixed)
            ans *= K - fixed
            ans %= MOD
        for next in G[cur]:
            if next == pre:
                continue
            dfs(next, cur)
    dfs(0, -1)
    print(ans)
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
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)

if __name__ == '__main__':
    main()
