import math

class Seg:
    def __init__(self) -> None:
        pass
    
    def set(self, l: int, r: int) -> None:
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        return

class KthSmallest:
    def __init__(self, L: list):
       self.N = len(L)
       self.depth = int(math.log2(self.N)) + 1
       self.b = [[0 for _ in range(self.N)] for _ in range(self.depth)]
       self.b[0] = L
       self.left = [[0 for _ in range(self.N)] for _ in range(self.depth)]
       self.sortedL = sorted(L)
       self.segs = [Seg() for _ in range(self.N * 2)]
    
    def build(self, l: int = 0, r: int = None, depth: int = 0, idx: int = 1):
        if r is None:
            r = self.N
        self.segs[idx].set(l, r)
        if l + 1 == r:
            return
        mid = self.segs[idx].mid
        lsame = mid - l
        for i in range(l, r):
            if self.b[depth][i] < self.sortedL[mid]:
                lsame -= 1
        # print(lsame)
        lpos = l
        rpos = mid
        same = 0

        for i in range(l, r):
            if self.b[depth][i] < self.sortedL[mid]:
                self.b[depth + 1][lpos] = self.b[depth][i]
                lpos += 1
            elif self.b[depth][i] > self.sortedL[mid]:
                self.b[depth + 1][rpos] = self.b[depth][i]
                rpos += 1
            else:
                if same < lsame:
                    same += 1
                    self.b[depth + 1][lpos] = self.b[depth][i]
                    lpos += 1
                else:
                    self.b[depth + 1][rpos] = self.b[depth][i]
                    rpos += 1

        for i in range(l, r):
            self.left[depth][i] = self.left[depth][i-1] if i != l else 0
            if self.b[depth][i] < self.sortedL[mid]:
                self.left[depth][i] += 1
            else:
                if same < lsame:
                    self.left[depth][i] += 1
  
        for i in range(l, r):      
            self.build(l, mid, depth + 1, idx << 1)
            self.build(mid, r, depth + 1, idx << 1 | 1)

    def getKth(self, l: int, r: int, k: int, depth: int = 0, idx: int = 1):
        if l + 1 == r:
            return self.b[depth][l]
        ltl = self.left[depth][l - 1] if l != self.segs[idx].l else 0
        tl = self.left[depth][r - 1] - ltl

        if tl >= k:
            newl = self.segs[idx].l + ltl
            newr = self.segs[idx].l + ltl + tl
            return self.getKth(newl, newr, k, depth + 1, idx << 1)
        else:
            mid = self.segs[idx].mid
            tr = r - l - tl
            ltr = l - self.segs[idx].l - ltl
            newl = mid + ltr
            newr = mid + ltr + tr
            return self.getKth(newl, newr, k - tl, depth + 1, idx << 1 | 1)

    def rank(self, l: int, r: int, x: int, depth: int = 0, idx: int = 1):
        if self.segs[idx].l + 1 == self.segs[idx].r:
            return l + 1 == r and self.sortedL[l] <= x
        ltl = self.left[depth][l - 1] if l != self.segs[idx].l else 0
        tl = self.left[depth][r - 1] - ltl
        mid = self.segs[idx].mid
        if x < self.sortedL[mid]:
            newl = self.segs[idx].l + ltl
            newr = self.segs[idx].l + ltl + tl
            return self.rank(newl,newr,x,depth+1,idx<<1)
        else:
            tr = r - l - tl
            ltr = l - self.segs[idx].l - ltl
            newl = mid + ltr
            newr = mid + ltr + tr
            return tl + self.rank(newl,newr,x,depth+1,idx<<1|1)

# a = [6,12,5,17,10,2,7,3]
# a = [1,1,5,6,1,1,7,8]
# a = [2,2,2,2,1,1,3,3]
# # a = [1,1,1,1,1,6,7,8]
# ks = KthSmallest(a)
# ks.build()
# print(ks.b)
# print(ks.getKth(2, 7, 3))
# print(ks.rank(2, 7, 7))
l = []
import time
# for i in range(5):
#     l.extend([10 ** i] * ((10 ** 5) // (2 ** (5 - i))))
    # print([10 ** i], ((10 ** 5) // (2 ** (5 - i))))
# l = [1,10,10,100,100,100,100,1000,1000,1000,1000,1000,1000,1000,1000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
l = [1,10,9,2,8,3,100,7]
start = time.time()
for i in range(10):
    ks = KthSmallest(l)
    ks.build()
    print(ks.b)
end = time.time()
print(end - start)
    

# struct KthSmallest {
#   struct Seg {
#     int l, r, mid;
#     void set(int _l, int _r) {
#       l = _l; r = _r;
#       mid = l+r>>1;
#     }
#   } seg[N<<2];
#   int b[25][N], left[25][N], sorted[N];
#   void init(int *a, int n) {
#     for (int i=0; i<n; ++i) b[0][i] = sorted[i] = a[i];
#     sort(sorted, sorted+n);
#     build(0,n,0,1);
#   }
#   void build(int l, int r, int d, int idx) {
#     seg[idx].set(l,r);
#     if (l+1 == r) return;
#     int mid = seg[idx].mid;
#     int lsame = mid - l;
#     for (int i=l; i<r; ++i)
#       if (b[d][i] < sorted[mid])
#         lsame--;
#     int lpos = l, rpos = mid, same = 0;
#     for (int i=l; i<r; ++i) {
#       left[d][i] = (i!=l ? left[d][i-1] : 0);
#       if (b[d][i] < sorted[mid]) {
#         left[d][i]++;
#         b[d+1][lpos++] = b[d][i];
#       } else if (b[d][i] > sorted[mid]) {
#         b[d+1][rpos++] = b[d][i];
#       } else {
#         if (same < lsame) {
#           same++;
#           left[d][i]++;
#           b[d+1][lpos++] = b[d][i];

#         } else {
#           b[d+1][rpos++] = b[d][i];
#         }
#       }
#     }
#     build(l,mid,d+1,idx<<1);
#     build(mid,r,d+1,idx<<1|1);
#   }
#   /*
#     [l,r)をソートしたときk番目に来る値は何か
#    */
#   int kth(int l, int r, int k, int d=0, int idx=1) { // k : 1-origin!!!
#     if (l+1 == r) return b[d][l];
#     int ltl = (l!=seg[idx].l ? left[d][l-1] : 0);
#     int tl = left[d][r-1] - ltl;

#     if (tl >= k) {
#       int newl = seg[idx].l + ltl;
#       int newr = seg[idx].l + ltl + tl;
#       return kth(newl,newr,k,d+1,idx<<1);
#     } else {
#       int mid = seg[idx].mid;
#       int tr = r - l - tl;
#       int ltr = l - seg[idx].l - ltl;
#       int newl = mid + ltr;
#       int newr = mid + ltr + tr;
#       return kth(newl,newr,k-tl,d+1,idx<<1|1);
#     }
#   }
#   /*
#     [l,r)をソートしたときxは何番目に来るか．
#     xが2つ以上あるときは，最後のもののrankを返す．
#     xがないときはx未満で最大なもののrankを返す．
#     x未満がないときは0を返す．
#   */ 
#   int rank(int l, int r, int x, int d=0, int idx=1) {
#     if (seg[idx].l+1 == seg[idx].r) {
#       return l+1==r&&sorted[l]<=x;
#     }
#     int ltl = (l!=seg[idx].l ? left[d][l-1] : 0);
#     int tl = left[d][r-1] - ltl;
#     int mid = seg[idx].mid;
#     if (x < sorted[mid]) {
#       int newl = seg[idx].l + ltl;
#       int newr = seg[idx].l + ltl + tl;
#       return rank(newl,newr,x,d+1,idx<<1);
#     } else {
#       int tr = r - l - tl;
#       int ltr = l - seg[idx].l - ltl;
#       int newl = mid + ltr;
#       int newr = mid + ltr + tr;
#       return tl + rank(newl,newr,x,d+1,idx<<1|1);
#     }
#   }
#   /*
#     [l,r)にxは何個あるか
#   */ 
#   int freq(int l, int r, int x) {
#     return rank(l,r,x)-rank(l,r,x-1);
#   }
# } kth;

# int main() {
#   int a[8] = {6,12,5,17,10,2,7,3};
#   kth.init(a, 8);
#   cout << kth.kth(2,7,3) << endl; // 7
#   cout << kth.rank(2,7,7) << endl; // 3
# }   