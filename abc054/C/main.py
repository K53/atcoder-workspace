#!/usr/bin/env python3
import sys

def main():    
    N, M = 0, 0
    edge = []

    # -------------------------------------------
    # Parameters
    #      visited : 訪問済みリスト(0/1)
    #      s       : 訪問する頂点
    # -------------------------------------------
    def dfs(visited: "List[int]", s: int):
        count = 0
        for i in edge[s]:           # その頂点sに繋がる頂点全てについて到達可能な場所を調べる。
            if sum(visited) == N:
                return 1            # そのルートが条件を満たすので1つカウント
            if not visited[i]:      # 未到達なら"新しくvisitedリストを生成してdfsに渡す。
                count += dfs(visited[:i] + [1] + visited[i + 1:], i)  # stackでやろうとするとこの分岐の都度スタックと訪問済みフラグを生成する必要があってわけわかんなくなる。
        return count

    N, M = map(int, input().split())
    visited = [0] * N               # 訪問済みフラグ(0/1)
    edge = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    
    visited[0] = 1
    ans = dfs(visited, 0)
    print(ans)
    return

if __name__ == '__main__':
    main()
