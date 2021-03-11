#!/usr/bin/env python3
import sys

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n # 根は自分を含めて下に何個の要素がぶら下がっているかが負の数で表される。
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    # 要素xの属する集合の要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    
    # 要素x,yが同じ集合かを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # 集合の数を返す
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, M = map(int, input().split())
    A, B = [], []
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(lambda i : int(i) - 1, input().split())
        A.append(a)
        B.append(b)
    
    ans = [N * (N - 1) // 2]
    for a, b in zip(A[::-1], B[::-1]):
        if uf.same(a, b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] - uf.size(a) * uf.size(b))
            uf.union(a, b)
    # print(ans)
    ans = ans[:-1]
    print(*ans[::-1], sep="\n")
        


if __name__ == '__main__':
    main()
