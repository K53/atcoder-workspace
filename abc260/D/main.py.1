#!/usr/bin/env python3
import sys
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.group_num = n
        self.parents = [-1] * n

    """ 要素xの値を取得。"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    """ 2つの要素の併合。"""
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.group_num -= 1
        return

    """ 要素xの属する集合の要素数を取得。"""
    def size(self, x):
        return -self.parents[self.find(x)]

    """ 2つの要素が同一の集合に属するか。"""
    def same(self, x, y):
        return self.find(x) == self.find(y)

    """ 要素xと同一の集合の要素を全取得。
    計算量 : O(N)
    """
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    """ 各集合の根を全取得。
    計算量 : O(N)
    """
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    """ 集合の個数を取得。 v2
    計算量 : O(1)
    """
    def group_count_v2(self):
        return self.group_num

    """ 集合の個数を取得。 v1
    計算量 : O(N)
    """
    def group_count_v1(self):
        return len(self.roots())

    """ 全集合の要素一覧を取得。
    計算量 : O(N)
    """
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    


def solve(N: int, K: int, P: "List[int]"):
    # N = 2 * 10 ** 5
    # K = 3
    # P = list(reversed(range(1, N + 1)))
    import bisect

    class BIT:

        def __init__(self,len_A):
            self.N = len_A + 10
            self.bit = [0]*(len_A+10)
            
        # sum(A0 ~ Ai)
        # O(log N)
        def query(self,i):
            res = 0
            idx = i+1
            while idx:
                res += self.bit[idx]
                idx -= idx&(-idx)
            return res

        # Ai += x
        # O(log N)
        def update(self,i,x):
            idx = i+1
            while idx < self.N:
                self.bit[idx] += x
                idx += idx&(-idx)
        
        # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
        # O(log N)
        def lower_left(self,w):
            if (w < 0):
                return -1
            x = 0
            k = 1<<(self.N.bit_length()-1)
            while k > 0:
                if x+k < self.N and self.bit[x+k] < w:
                    w -= self.bit[x+k]
                    x += k
                k //= 2
            return x


    class OrderBIT:

        def __init__(self,all_values,sort_flag = False):
            if sort_flag:
                self.A = all_values
            else:
                self.A = sorted(all_values)
            self.B = BIT(len(all_values))
            self.num = 0
            
        def insert_val(self,x,c=1):
            k = bisect.bisect_left(self.A,x)
            self.B.update(k,c)
            self.num += c
        
        def delete_val(self,x,c=1):
            k = bisect.bisect_left(self.A,x)
            self.B.update(k,-c)
            self.num -= c
        
        # find the k-th min_val (k:0-indexed)
        def find_kth_val(self,k):
            if self.num <= k:
                ##### MINIMUM VAL #######
                return (-10**9, -1)
            return (self.A[self.B.lower_left(k+1)], self.B.lower_left(k+1))
        
        # count the number of values lower than or equal to x
        def count_lower(self,x):
            if x < self.A[0]:
                return 0
            return self.B.query(bisect.bisect_right(self.A,x)-1)

        # min_val higher than x
        def find_higher(self,x):
            return self.find_kth_val(self.count_lower(x))
    ans = [-1] * N
    if K == 1:
        ans[P[0] - 1] = 1
    d = dict()
    uf = UnionFind(N + 1)
    bt = OrderBIT(range(1,N + 1), sort_flag=True)
    # for i in range(N):
    #     res = bt.insert_val(P[i])
    for i in range(N):
        res = bt.find_higher(P[i])
        # print(res)
        if res[0] == -1000000000:
            if uf.size(P[i]) != K:
                # print(i, res)
                bt.insert_val(P[i])
            else:
                # print(uf.find(P[i]))
                rr = uf.find(P[i])
                d[rr] = i + 1
        else: 
            # print(i, res)
            uf.union(res[0], P[i])
            if uf.size(P[i]) != K:
                bt.delete_val(res[0])
                bt.insert_val(P[i])
            else:
                bt.delete_val(res[0])
                rr = uf.find(P[i])
                d[rr] = i + 1
    # print(avl_key)
    for r, g in uf.all_group_members().items():
        if r in d:
            for gg in g:
                ans[gg - 1] = d[r]
        # print(g)
    # print(d)
    print(*ans, sep="\n")
    
    # for i in range(N):
    #     turn = i + 1
    #     bisect.bi
    #     P[i]

        
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, P)

if __name__ == '__main__':
    main()
