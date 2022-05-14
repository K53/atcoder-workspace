#!/usr/bin/env python3
import sys
def fibonacci_list(n):
    fib = [1, 1, 2]
    if n == 1:
        fib = [1]
    else:
        for k in range(3, n):
            a = fib[k-1]+fib[k-2]+fib[k-3]
            fib.append(10 ** 6 if a > 10 ** 6 else a)
    return fib
def solve(W: int):
    print(300)
    print(*fibonacci_list(300), sep=" ")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    solve(W)

if __name__ == '__main__':
    main()