#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, A: "List[int]"):
    # l = [0] * 4
    # for aa in A:
    #     l[0] = 1
    #     for i in range(4):
    #         if l[i]:

    #             l[i + aa]
    p = 0
    aa = list(itertools.accumulate(A[::-1]))
    for aaa in aa:
        if aaa >= 4:
            p += 1
    print(p)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()