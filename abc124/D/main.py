#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S: str):
    from itertools import groupby
    def runLengthEncode(S: str) -> "List[tuple(str, int)]":
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res
    ss = runLengthEncode(S)
    # print(ss)

    l = 0
    r = 0
    count = K
    length = 0
    ans = 0
    f = True
    N = len(ss)
    for _ in range(N):
        while r < N and f:
            # print("#", l, r, length)
            if ss[r][0] == "0":
                if count == 0:
                    f = False
                    ans = max(ans, length)
                    break
                count -= 1
            length += ss[r][1]
            r += 1
        if not f:
            # print(">", l, r, length)
            if ss[l][0] == "0":
                count += 1
                f = True
            length -= ss[l][1]
            l += 1
    ans = max(ans, length)
    print(ans)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)

if __name__ == '__main__':
    main()
