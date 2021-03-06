#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    for hh in range(H):
        for ww in range(W):
            A[hh][ww] -= B[hh][ww]

    
    ans = 0
    for hh in range(H - 1):
        for ww in range(W - 1):
            if A[hh][ww] == 0:
                continue
            d = -A[hh][ww]
            A[hh][ww] += d
            A[hh][ww + 1] += d
            A[hh + 1][ww] += d
            A[hh + 1][ww + 1] += d
            ans += abs(d)

    for hh in range(H):
        for ww in range(W):
            if A[hh][ww] != 0:
                print(NO)
                return
    print(YES)
    print(ans)
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A, B)

if __name__ == '__main__':
    main()
