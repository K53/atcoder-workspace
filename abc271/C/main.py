#!/usr/bin/env python3
import sys
from collections import deque

def solve(N: int, a: "List[int]"):
    s = set(a)
    dup = N - len(s)
    ex = [10 ** 9 + 1 + i for i in range(dup)]
    s = sorted(list(s))
    s.extend(ex)
    q = deque(s)
    next = 1
    while len(q) != 0:
        head = q[0]
        if head == next:
            q.popleft()
            next += 1
            continue
        if len(q) >= 2:
            q.pop()
            q.pop()
            next += 1
            continue
        break
    print(next - 1)
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