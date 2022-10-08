#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[str]"):
    for y in range(N):
        for x in range(y, N):
            if y == x:
                if A[y][x] != "-":
                    print("incorrect")
                    return
            else:
                if (A[y][x] == A[x][y] == "D") or (A[y][x] == "W" and A[x][y] == "L") or (A[y][x] == "L" and A[x][y] == "W"):
                    continue
                else:
                    print("incorrect")
                    return
    print("correct")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, A)

if __name__ == '__main__':
    main()