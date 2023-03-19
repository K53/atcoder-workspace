#!/usr/bin/env python3
import sys


def solve(X: int):
    ans = 1
    for b in range(1, X):
        now = b
        for p in range(2, 10):
            if now * b > X:
                if p == 2:
                    break
                ans = max(ans, now)
                break
            now *= b
    print(ans)
    
            

                
            
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
