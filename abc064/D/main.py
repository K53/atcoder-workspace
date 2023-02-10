#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    ans1 = 0
    k = [0]
    for i in range(N):
        if S[i] == ")":
            k.append(k[-1] - 1)
        else:
            k.append(k[-1] + 1)
    ans1 += 0 - min(k)
    ans2 = 0
    k = [0]
    for i in range(N):
        if S[::-1][i] == "(":
            k.append(k[-1] - 1)
        else:
            k.append(k[-1] + 1)
    ans2 += 0 - min(k)
    print("(" * ans1 + S + ")" * ans2)
    return


    # )(())))(
    
    # 0-1010-1-2-3-2
    # 0-10123212

    # (()((((()))(
    
    # 0121234565434

    


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
