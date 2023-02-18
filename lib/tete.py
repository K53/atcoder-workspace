def segfunc(x,y):
    return x+y
class LazySegTree_RAQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [0]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v==0:
                continue
            self.lazy[i] = 0
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.tree[2*i] += v
            self.tree[2*i+1] += v
    def add(self,l,r,x):
        ids = self.gindex(l,r)
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r&1:
                self.lazy[r-1] += x
                self.tree[r-1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]
    def query(self,l,r):
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


seg = LazySegTree_RAQ([0, 1, 4, 9, 2, 5, 3, 1],segfunc,0)
print(seg.tree)

seg.add(1, 4, 4)
print(seg.lazy)
print(seg.tree)



[0,       25,
    14,        11, 
 1,    13,   7,    4, 
0, 1, 4, 9, 2, 5, 3, 1]

[0,       33,
    22,         11, 
  5,   17,    7,  4,
0, 5, 4, 9, 2, 5, 3, 1]



[0,       0,
     0,        0, 
  0,    4,   0,    0, 
0, 4, 0, 0, 0, 0, 0, 0]

ans = seg.query(0, 1)
print(ans) # 5 22
ans = seg.query(0, 2)
print(ans) # 5 22
ans = seg.query(0, 3)
print(ans) # 5 22
ans = seg.query(0, 4)
print(ans) # 5 22