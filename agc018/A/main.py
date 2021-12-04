#!/usr/bin/env python3
import sys

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str


def solve(N: int, K: int, A: "List[int]"):
    import functools 
    import math
    g = functools.reduce(math.gcd, A)
    if K > max(A):
        print(NO)
        return
    print(YES if K % g == 0 else NO)
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
