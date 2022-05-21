#!/usr/bin/env python3
from collections import Counter
import sys

MOD = 10  # type: int


def solve(N: int, S: "List[str]"):
    d = [[] for _ in range(10)]
    for ss in S:
        for i in range(10):
            d[int(ss[i])].append(i)
    # for i in range(10):
    #     print(d[i])
    # print()
    ans = []
    for i in range(10):
        c = Counter(d[i])
        l = []
        for num, count in c.items():
            l.append(num + 10 * (count - 1))
        # print(l)
        ans.append(max(l))
    print(min(ans))
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
