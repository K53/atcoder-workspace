#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, M: int, A: "List[str]", B: "List[str]"):
    def check(sx, sy):
        for dy in range(M):
            for dx in range(M):
                if sy + dy >= N or sx + dx >= N:
                    return False
                if not A[sy + dy][sx + dx] == B[dy][dx]:
                    return False
        print(YES)
        return True
    
    for sy in range(N):
        for sx in range(N):
            if check(sx, sy):
                return
    print(NO)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    B = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
