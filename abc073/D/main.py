#!/usr/bin/env python3
import sys


def solve(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    INF = 10 ** 16
    class WarshallFloyd():
        def __init__(self, N):
            self.N = N
            dp = [[INF] * N for _ in range(N)]
            for i in range(N):
                dp[i][i] = 0
            self.dp = dp
        
        # 自己ループを持つグラフの扱いは注意。
        def addEdge(self, fromNode: int, toNode: int, cost: int = 1):
            self.dp[fromNode][toNode] = cost
        
        def build(self):
            for via in range(self.N):
                for start in range(self.N):
                    for goal in range(self.N):
                        self.dp[start][goal] = min(self.dp[start][goal], self.dp[start][via] + self.dp[via][goal])
            return self.dp
    wf = WarshallFloyd(N)
    for aa, bb, cc in zip(A, B, C):
        wf.addEdge(aa - 1, bb - 1, cc)
        wf.addEdge(bb - 1, aa - 1, cc)
    d = wf.build()
    import itertools
    ans = INF
    for rr in itertools.permutations(r):
        res = 0
        for i in range(R - 1):
            res += d[rr[i]][rr[i + 1]]
        ans = min(ans, res)
    print(ans)
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    r = [int(next(tokens)) - 1 for _ in range(R)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, R, r, A, B, C)

if __name__ == '__main__':
    main()
