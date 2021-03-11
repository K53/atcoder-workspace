```python
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
```

https://atcoder.jp/contests/abc177/tasks/abc177_d
https://atcoder.jp/contests/arc032/tasks/arc032_2
https://atcoder.jp/contests/abc120/tasks/abc120_d
https://atcoder.jp/contests/abc157/tasks/abc157_d

```py
def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(lambda i : int(i) - 1, input().split())
        uf.union(a, b)
    ans = 0
    for i in range(N):
        ans = max(ans, uf.size(i))
    print(ans)

if __name__ == '__main__':
    main()
```

