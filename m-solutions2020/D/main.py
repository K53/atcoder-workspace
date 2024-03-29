#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    coin = 1000
    stock = 0
    for i in range(N - 1):
        if A[i] < A[i + 1]:
            p, q = divmod(coin, A[i])
            stock += p
            coin = q
        coin += stock * A[i + 1]
        stock = 0
        # print(stock, coin)
    print(coin)
    
        
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
