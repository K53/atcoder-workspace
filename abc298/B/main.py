#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: "List[List[int]]", B: "List[List[int]]"):
    for i in range(4):
        k = 0
        for i in range(N):
            for j in range(N):
                if A[i][j] == 0 or A[i][j] == B[i][j] == 1:
                    k += 1
        if k == N ** 2:
            print(YES)
            return
        A = list(zip(*A[::-1]))
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
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
