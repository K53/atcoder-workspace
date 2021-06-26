#!/usr/bin/env python3
import sys


def solve(N: int, T: "List[int]"):
    # N = 100
    # T = [1000] * 100
    # ans = 10 ** 9
    # for i in range(2 ** N):
    #     a = 0
    #     b = 0
    #     for bb in range(N):
    #         if i >> bb & 1:
    #             a += T[bb]
    #         else:
    #             b += T[bb]
    #     # print(max(a, b))
    #     ans = min(ans, max(a, b))
    # print(ans)
    dp = [[0] * (10 ** 5 + 10) for _ in range(N)]
    dp[0][T[0]] = 1
    for i in range(1, N):
        dp[i][T[i]] = 1
        for tt in range(10 ** 5 + 10):
            if dp[i - 1][tt]:
                dp[i][tt] = 1
                if tt + T[i] < 10 ** 5 + 10: 
                    dp[i][tt + T[i]] = 1
    ss = sum(T)
    center = ss // 2 + ss % 2
    if dp[N - 1][center]:
        print(center)
        return
    for d in range((10 ** 5) // 2 + 1):
        if center + d < 10 ** 5 + 10 and dp[N - 1][center + d]:
            print(center + d)
            return
        if center - d > 0 and dp[N - 1][center - d]:
            print(center - d)
            return

    
    # print(dp[0][:25])
    # print(dp[1][:25])
    # print(dp[2][:25])
    # print(dp[3][:25])
    # print(dp[4][:25])

        
    

    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)

if __name__ == '__main__':
    main()