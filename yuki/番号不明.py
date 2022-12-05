#!/usr/bin/env python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

def main():
    N, K = map(int, input().split())
    G = [[] for _ in range(N)] # 隣接リスト
    edges = defaultdict(lambda: defaultdict(int))
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        G[a - 1].append((b - 1, c))
        G[b - 1].append((a - 1, c))

    alt = []
    seen = [0] * N
    def dfs(pre: int, now: int, cost: int):
        count = 1
        # print(pre, now)
        # [2] 
        # そのノードに初めて到着した時のみ
        # <<== 行きがけ順ならここを使う (初めて降り立つ時にしか実行されない)
        seen[now] = 1 # 訪問済みにする #開始点もseenにしないといけないのでfor前にフラグを立てる。
        # --- 子ノードを探索 -----------------------
        for next, c in G[now]: 
            # --- 遷移前に訪問済みチェック ----------- # 木であれば "next == pre" で判定でも可
            if seen[next] == 1: 
                continue
            # [1]
            # そのノードから子ノードに向かって出発しようとした時
            count += dfs(now, next, c)
            # [4]
            # そのノードに子ノードから帰ってきて到着した時
            # <== 木上のDPをする時はここを使うこと。
            # <== 領域[3]を使うと子から帰る時に親を操作するようになり直感に反する(あと1頂点のみのケースとかで例外処理が面倒)。
        # [3]
        # そのノードから親ノードに帰ろうと出発した時
        # <<== 帰りがけ順ならここを使う
        edges[pre][now] = count
        if pre != -1:
            alt.append((cost, count * cost))
        return count
    
    dfs(pre=-1, now=0, cost=0)
    for k, v in edges.items():
        print(k, v)
    print(alt)
    dp = [[0 for _ in range(N)] for _ in range(K)]
    for i in range(N - 1):
        for j in range(K):






if __name__ == '__main__':
    main()




###
#!/usr/bin/env python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

def main():
    N, K = map(int, input().split())
    G = [[] for _ in range(N)] # 隣接リスト
    edges = defaultdict(lambda: defaultdict(int))
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    seen = [0] * N
    p = [0] * N # 部分木のサイズ
    def dfs(pre: int, now: int):
        count = 1
        # print(pre, now)
        # [2] 
        # そのノードに初めて到着した時のみ
        # <<== 行きがけ順ならここを使う (初めて降り立つ時にしか実行されない)
        seen[now] = 1 # 訪問済みにする #開始点もseenにしないといけないのでfor前にフラグを立てる。
        # --- 子ノードを探索 -----------------------
        for next in G[now]: 
            # --- 遷移前に訪問済みチェック ----------- # 木であれば "next == pre" で判定でも可
            if seen[next] == 1: 
                continue
            # [1]
            # そのノードから子ノードに向かって出発しようとした時
            count += dfs(now, next)
            # [4]
            # そのノードに子ノードから帰ってきて到着した時
            # <== 木上のDPをする時はここを使うこと。
            # <== 領域[3]を使うと子から帰る時に親を操作するようになり直感に反する(あと1頂点のみのケースとかで例外処理が面倒)。
        # [3]
        # そのノードから親ノードに帰ろうと出発した時
        # <<== 帰りがけ順ならここを使う
        p[now] = count
        return count
    
    dfs(pre=-1, now=0)
    print(p)




if __name__ == '__main__':
    main()




### 
#!/usr/bin/env python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

def main():
    N, K = map(int, input().split())
    G = [[] for _ in range(N)] # 隣接リスト
    edges = defaultdict(lambda: defaultdict(int))
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    seen = [0] * N
    p = [0] * N
    def dfs(pre: int, now: int):
        count = 1
        # print(pre, now)
        # [2] 
        # そのノードに初めて到着した時のみ
        # <<== 行きがけ順ならここを使う (初めて降り立つ時にしか実行されない)
        seen[now] = 1 # 訪問済みにする #開始点もseenにしないといけないのでfor前にフラグを立てる。
        # --- 子ノードを探索 -----------------------
        for next in G[now]: 
            # --- 遷移前に訪問済みチェック ----------- # 木であれば "next == pre" で判定でも可
            if seen[next] == 1: 
                continue
            # [1]
            # そのノードから子ノードに向かって出発しようとした時
            count += dfs(now, next)
            # [4]
            # そのノードに子ノードから帰ってきて到着した時
            # <== 木上のDPをする時はここを使うこと。
            # <== 領域[3]を使うと子から帰る時に親を操作するようになり直感に反する(あと1頂点のみのケースとかで例外処理が面倒)。
        # [3]
        # そのノードから親ノードに帰ろうと出発した時
        # <<== 帰りがけ順ならここを使う
        edges[pre][now] = count
        return count
    
    dfs(pre=-1, now=0)
    for k, v in edges.items():
        print(k, v)




if __name__ == '__main__':
    main()