#!/usr/bin/env python3
import sys


def solve():
    # a < b < c
    # b 全探索 10 ** 5
    # 
    K = int(input())
    ans = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            if a * b > K:
                break
            p, q = divmod(K, a * b)
            ans += p
    print(ans)
    return


# # Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
# def main():
#     def iterate_tokens():
#         for line in sys.stdin:
#             for word in line.split():
#                 yield word
#     tokens = iterate_tokens()
#     K = int(next(tokens))  # type: int
#     solve(K)

if __name__ == '__main__':
    solve()
