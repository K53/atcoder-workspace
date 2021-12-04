#!/usr/bin/env python3
import sys
MOD = 1000000007  # type: int


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    H, W = map(int, sys.stdin.readline().split())
    S = [sys.stdin.readline()[:-1] for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    xsdp = [[0] * W for _ in range(H)]
    ysdp = [[0] * W for _ in range(H)]
    zsdp = [[0] * W for _ in range(H)]
    for hh in range(H):
        for ww in range(W):
            if hh == 0 and ww == 0:
                continue
            if S[hh][ww] == "#":
                continue
            if ww - 1 >= 0:
                xsdp[hh][ww] = (xsdp[hh][ww - 1] + dp[hh][ww - 1]) % MOD
            if hh - 1 >= 0:
                ysdp[hh][ww] = (ysdp[hh - 1][ww] + dp[hh - 1][ww]) % MOD
            if hh - 1 >= 0 and ww - 1 >= 0:
                zsdp[hh][ww] = (zsdp[hh - 1][ww - 1] + dp[hh - 1][ww - 1]) % MOD
            dp[hh][ww] = (xsdp[hh][ww] + ysdp[hh][ww] + zsdp[hh][ww]) % MOD
    
    # for i in range(H):
    #     print(xsdp[i])
    # print("===")
    # for i in range(H):
    #     print(ysdp[i])
    # print("===")
    # for i in range(H):
    #     print(zsdp[i])
    # print("===")
    # for i in range(H):
    #     print(dp[i])
    print(dp[-1][-1] % MOD)
    return

if __name__ == '__main__':
    main()
