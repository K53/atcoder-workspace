#!/usr/bin/env python3
import sys
from collections import defaultdict

def solve(N: int, A: "List[int]"):
    ans = 0
    d = defaultdict(int)
    for i in A:
        d[i] += 1
    for aa in range(N):
        all = N - 1 - aa
        ans += all - (d[A[aa]] - 1)
        d[A[aa]] -= 1
        # print(d)
    print(ans)
    
    
    # ans = 0
    # for i in range(N - 1):
    #     for j in range(i, N):
    #         if A[i] == A[j]:
    #             ans += 1
    # print(ans)
                
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
