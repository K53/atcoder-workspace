#!/usr/bin/env python3
import sys
import heapq

def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    a.sort()
    b.sort()
    q = []
    ans = []
    selected = set()
    heapq.heappush(q, (a[0] * b[0], 0, 0))
    for i in range(K):
        e, aa, bb = heapq.heappop(q)
        ans.append(e)
        for ia, ib in [(1, 0), (0, 1)]:
            if aa + ia < N and bb + ib < N and not (aa + ia, bb + ib) in selected:
                heapq.heappush(q, (a[aa + ia] * b[bb + ib], aa + ia, bb + ib))
                selected.add((aa + ia, bb + ib))
    print(ans[-1])
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a, b)

if __name__ == '__main__':
    main()
