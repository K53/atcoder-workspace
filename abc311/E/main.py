#!/usr/bin/env python3
import sys

def solve(H: int, W: int, N: int, a: "List[int]", b: "List[int]"):
    isEmp = [[0] * W for _ in range(H)]
    for aa, bb in zip(a, b):
        isEmp[aa - 1][bb - 1] = 1
    
    dp = [[0] * W for _ in range(H)]
    for hh in range(H):
        if isEmp[hh][0]:
            continue
        dp[hh][0] = 1
    for ww in range(W):
        if isEmp[0][ww]:
            continue
        dp[0][ww] = 1
    

    for hh in range(1, H):
        for ww in range(1, W):
            if isEmp[hh][ww]:
                continue
            if isEmp[hh - 1][ww - 1]:
                dp[hh][ww] = 1
            else:
                lw = ww - dp[hh - 1][ww - 1] 
                can = dp[hh - 1][ww - 1] + 1
                for i in reversed(range(lw, ww)):
                    if isEmp[hh][i]:
                        can = min(can, ww - i)
                        break
                lh = hh - dp[hh - 1][ww - 1] 
                for i in reversed(range(lh, hh)):
                    if isEmp[i][ww]:
                        can = min(can, hh - i)
                        break
                
                dp[hh][ww] = can

    # for hh in range(H):
    #     print(dp[hh])
    ans = 0
    for hh in range(H):
        for ww in range(W):
            ans += dp[hh][ww]
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(H, W, N, a, b)

if __name__ == '__main__':
    main()
