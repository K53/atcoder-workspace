#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

def conv(s: str):
    d = 0
    res = 0
    for t in s[::-1]:
        n = ord(t)
        if n <= ord("Z"):
            res += (n - ord("A") + 1) * (52 ** d)
        else:
            res += (n - ord("a") + 1 + 26) * (52 ** d)
        d += 1
    return res

def solve(N: int, s: "List[str]"):
    G = [[] for _ in range(52 ** 3 + 1)]
    dp = [-1] * (52 ** 3 + 1)
    for i in s:
        G[conv(i[:3])].append(conv(i[-3:]))
    # print(G[conv("abc")])
    # print(conv("bcd"))
    # print(G[conv("bcd")])
    # print(conv("cda"))
    # print(G[conv("ada")])
    # print(conv("ada"))
    for node in len(G):
        if len(G[node]) == 0:
            dp[node] = 0
    


        
    

        

    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
