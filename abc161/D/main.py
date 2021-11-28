#!/usr/bin/env python3
import sys
from collections import deque

def solve(K: int):
    q = deque()
    for i in range(9):
        q.append(i + 1)
    ans = []
    for i in range(K):
        now = q.popleft()
        ans.append(now)
        kk = now % 10
        if kk == 0:
            q.append(now * 10 + 0)
            q.append(now * 10 + 1)
        elif kk == 9:
            q.append(now * 10 + 8)
            q.append(now * 10 + 9)
        else:
            q.append(now * 10 + kk - 1)
            q.append(now * 10 + kk)
            q.append(now * 10 + kk + 1)
        
    print(ans[K - 1])
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()
