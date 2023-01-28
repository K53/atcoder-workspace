#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    # S = ["k"] * (5 * 10 ** 5)
    # N = len(S)
    
    maxS = 0
    for i in range(N):
        maxS = max(maxS, len(S[i]))
    l = [[set() for _ in range(26)] for _ in range(N)]
    for i in range(N):
        for j in range(maxS):
            if j >= len(S[i]):
                continue
            l[j][ord(S[i][j]) - ord("a")].add(i)
    # for j in range(maxS):
    #     print(l[j])

    ans = []
    for i in range(N):
        chr = ord(S[i][0]) - ord("a")
        ok = l[0][chr] | set()
        # if i == 10:
        #     print(ok)
        if len(ok) == 1:
            ans.append(0)
            continue
        if len(S[i]) == 1:
            ans.append(1)
            continue
        for j in range(1, len(S[i])):
            chr = ord(S[i][j]) - ord("a")
            now = l[j][chr]
            # if i == 9:
            #     print(now)
            ok &= now
            # if i == 9:
            #     print(ok)
            if len(ok) == 1:
                ans.append(j)
                break
        else:
            ans.append(j + 1)
    print(*ans, sep="\n")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
