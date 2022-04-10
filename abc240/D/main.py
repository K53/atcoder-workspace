#!/usr/bin/env python3
from collections import deque
import sys


def solve(N: int, a: "List[int]"):
    q = deque()
    tot = 0
    for aa in a:
        if len(q) == 0:
            q.append((aa, 1))
            tot += 1
            print(tot)
            continue
        # print(q)
        ch, num = q.pop()
        if ch == aa:
            if num + 1 != ch:
                q.append((aa, num + 1))
                tot += 1
            else:
                tot -= num
        else:
            q.append((ch, num))
            q.append((aa, 1))
            tot += 1
        print(tot)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()