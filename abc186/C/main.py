#!/usr/bin/env python3
import sys

    
def solve(N: int):
    ans = 0
    for i in range(1, N + 1):
        if "7" in str(i) or "7" in str(oct(i)):
            continue
        ans += 1
    print(ans)
        


    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
