#!/usr/bin/env python3
import sys
from itertools import permutations

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, S: "List[str]"):
    for case in permutations(range(N)):
        for i in range(N - 1):
            c = 0
            for num in range(M):
                if S[case[i]][num] != S[case[i + 1]][num]:
                    c += 1
            if c != 1:
                break
        else:
            print(YES)
            return
    print(NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, M, S)

if __name__ == '__main__':
    main()