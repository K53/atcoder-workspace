#!/usr/bin/env python3
import sys
import heapq

def solve(N: int, L: int, A: "List[int]"):
    if L - sum(A) != 0:
        A.append(L - sum(A))
    heapq.heapify(A)
    cost = 0
    while len(A) != 1:
        aa = heapq.heappop(A)
        bb = heapq.heappop(A)
        cost += aa + bb
        heapq.heappush(A, aa + bb)
    # last = heapq.heappop(A)
    print(cost)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, A)

if __name__ == '__main__':
    main()