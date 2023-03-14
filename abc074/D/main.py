#!/usr/bin/env python3
import sys
INF = 10 ** 16

def solve(N: int, A: "List[List[int]]"):
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
            ans = 0
            """
            0 〜 (via - 1)までの地点だけを利用して求めたdpテーブルを使い、viaを経由地とした時の更新処理している。
            """
            for start in range(self.N - 1):
                for goal in range(start + 1, self.N):
                    min_dist =  INF # start - goal間の最短経路
                    for via in range(self.N):
                        if via == start or via == goal:
                            # 直接結ぶ道路が必要かを評価したいので経由地なしのパスを除外して最小値を見ている。
                            continue
                        min_dist = min(min_dist, self.dp[start][via] + self.dp[via][goal])
                    if self.dp[start][goal] > min_dist:
                        print(-1)
                        exit()
                    elif self.dp[start][goal] < min_dist:
                        # その直接結ぶ道路は必要とわかるので加算する。
                        ans += self.dp[start][goal]
            return ans
    wf = WarshallFloyd(N)
    for s in range(N - 1):
        for t in range(s + 1, N):
            wf.addEdge(s, t, A[s][t])
            wf.addEdge(t, s, A[s][t])
    ans = wf.build()
    print(ans)
    return

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)

if __name__ == '__main__':
    main()
