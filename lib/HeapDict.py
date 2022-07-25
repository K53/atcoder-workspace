# ------------------------------------------------------------------------------
#     logN削除付きHeapq
# ------------------------------------------------------------------------------
# 解説
# - 優先度付きキューでは最小値以外の要素にアクセス(参照/削除)できない。
# - そこで、最小要素をO(1)で取得できるheapqの性質を保ちながら任意要素の削除を可能としたもの。
# - multiset(C++)の二分探索できない版
# 
# リンク
# - https://tsubo.hatenablog.jp/entry/2020/06/15/124657
#
# Order
#   - insert() : 要素の挿入
#       - O(log(n))
#   - erase() : 要素の削除 <- point!
#       - O(log(n))
#       - 遅延削除を採用。heapqから任意の要素を削除することはできないため、dictで論理削除する。
#       - 先頭要素取得に影響しない場合は論理削除。影響する場合は物理削除し、次の先頭要素がすでに論理削除済みであれば遅延させていた物理削除を実行。(繰り返す)
#   - exist() : 要素の存在確認
#       - O(1)
#   - dryPop() : 最小値の参照(キューからの削除は伴わない)
#       - O(1)
# verify
# - https://atcoder.jp/contests/abc170/tasks/abc170_e
# - https://atcoder.jp/contests/abc253/tasks/abc253_c
# ------------------------------------------------------------------------------
import heapq
from collections import defaultdict
class HeapDict:
    def __init__(self):
        self.q=[]
        self.d=defaultdict(int)

    def insert(self, x):
        """要素xの挿入"""
        heapq.heappush(self.q, x)
        self.d[x] += 1

    def erase(self, x):
        """要素xの削除"""
        if self.d[x] == 0:
            print(x, " is not in HeapDict")
            return
        else:
            self.d[x] -= 1
        
        # 先頭から論理削除済みのものを物理削除する
        while len(self.q) != 0:
            if self.d[self.q[0]] == 0:
                heapq.heappop(self.q)
            else:
                break
    
    def isEmpty(self):
        """O(1)。キューが空かどうか。"""
        return len(self.q) != 0
    
    def size(self):
        """O(過去に出現した要素の種類n) : キューが空かどうかのみ知りたい場合はisEmpty()使用推奨"""
        return sum(self.d.values())

    def exist(self, x):
        """O(1)。要素の存在確認"""
        return self.d[x] != 0
    
    def getExistList(self):
        """キュー内の実際に存在する要素のみを返す(遅延削除のため、self.qだと削除済みでも残っている要素が表示される)"""
        return [i for i in self.q if self.exist(i)]

    def dryPop(self):
        """O(1)。先頭要素(通常は最小値)を返す。キューが空ならNoneを返す"""
        return self.q[0] if self.isEmpty() else None

    def __str__(self):
        """先頭要素取得に影響しない要素は遅延削除のため、キュー内に存在しているが事実上削除済みのものは括弧()書きしている"""
        return "[" + ", ".join([str(i) if self.exist(i) else "({})".format(i) for i in self.q]) + "]"

class HeapDictMax:
    def __init__(self):
        self.q=[]
        self.d=defaultdict(int)

    def insert(self, x):
        """要素xの挿入"""
        heapq.heappush(self.q, -x)
        self.d[-x] += 1

    def erase(self, x):
        """要素xの削除"""
        if self.d[-x] == 0:
            print(-x, " is not in HeapDict")
            return
        else:
            self.d[-x] -= 1

        # 先頭から論理削除済みのものを物理削除する
        while len(self.q) != 0:
            if self.d[self.q[0]] == 0:
                heapq.heappop(self.q)
            else:
                break
    
    def isEmpty(self):
        """O(1)。キューが空かどうか。"""
        return len(self.q) != 0
    
    def size(self):
        """O(過去に出現した要素の種類n) : キューが空かどうかのみ知りたい場合はisEmpty()使用推奨"""
        return sum(self.d.values())

    def exist(self, x):
        """O(1)。要素の存在確認"""
        return self.d[-x] != 0
    
    def getExistList(self):
        """O(len(self.q))。キュー内の実際に存在する要素のみを返す(遅延削除のため、self.qだと削除済みでも残っている要素が表示される)"""
        return [-i for i in self.q if self.exist(-i)]

    def dryPop(self):
        """O(1)。先頭要素(通常は最小値)を返す。キューが空ならNoneを返す"""
        return -self.q[0] if self.isEmpty() else None

    def __str__(self):
        """O(len(self.q))。先頭要素取得に影響しない要素は遅延削除のため、キュー内に存在しているが事実上削除済みのものは括弧()書きしている"""
        return "[" + ", ".join([str(-i) if self.exist(-i) else "({})".format(-i) for i in self.q]) + "]"


# usage
hq_min = HeapDict()
hq_max = HeapDictMax()

hq_min.insert(1)
hq_max.insert(1)
hq_min.insert(5)
hq_max.insert(5)
hq_min.insert(10)
hq_max.insert(10)
hq_min.insert(30)
hq_max.insert(30)

hq_min.erase(5) 
hq_max.erase(5)

print(hq_min) # [1, (5), 10, 30]
print(hq_max) # [30, 10, (5), 1]

hq_min.erase(1)
hq_max.erase(1)

print(hq_min) # [10, 30]
print(hq_max) # [30, 10, (5), (1)]

# 先頭要素取得。
print(hq_min.dryPop()) # 10
print(hq_max.dryPop()) # 30

# 論理削除済みのものを除いた全要素を返却。
print(hq_min.getExistList()) # [10, 30]
print(hq_max.getExistList()) # [30, 10]
