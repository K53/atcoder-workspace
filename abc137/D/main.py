#!/usr/bin/env python3
import sys
from collections import defaultdict
import heapq

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    d = defaultdict(list)
    for aa, bb in zip(A, B):
        d[aa].append(-bb)
    hq = []
    ans = 0
    heapq.heapify(hq)
    for last_day in range(M + 1):
        for score in d[last_day]:
            heapq.heappush(hq, score)
        if len(hq) > 0:
            ans += heapq.heappop(hq)
    print(-ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
