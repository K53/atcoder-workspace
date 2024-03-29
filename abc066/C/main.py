#!/usr/bin/env python3
import sys
from collections import deque

def solve(n: int, a: "List[int]"):
    b = deque()
    f = False
    for aa in a:
        if f:
            b.append(aa)
        else:
            b.appendleft(aa)
        f = not f
    b = list(b)
    if f:
        print(*b)
    else:
        print(*b[::-1])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
