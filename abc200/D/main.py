#!/usr/bin/env python3
import sys

MOD = 200  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, A: "List[int]"):
    mods = [0] * 200
    ansB = []
    ansC = []
    N = min(8, N)
    A = A[:N]
    for b in range(2 ** N):
        sum = 0
        for i in range(N):
            if b >> i & 1:
                sum += A[i] % MOD
        if mods[sum % 200] == 0:
            mods[sum % 200] = b
        else:
            print(YES)
            for i in range(N):
                if mods[sum % 200] >> i & 1:
                    ansB.append(i + 1)
                if b >> i & 1:
                    ansC.append(i + 1)
            print(len(ansB), *ansB, sep=" ")
            print(len(ansC), *ansC, sep=" ")
            return
    print(NO)

    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
