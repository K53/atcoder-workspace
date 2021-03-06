#!/usr/bin/env python3
import sys

def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    class MatrixAccumulates:
        def __init__(self, H: int, W: int) -> None:
            self.H, self.W = H, W
            self.LL = [[0] * W for _ in range(H)]
            self.S = []
        
        def add(self, y, x, val):
            self.LL[y][x] += val
            return

        def setList(self, LL: "List[List[int]]"):
            self.LL = LL
            return

        def build(self, index1: bool = False):
            if index1:
                self.S = [[0] * self.W for _ in range(self.H)]
                #ヨコに累積和
                for i in range(self.H):
                    for j in range(self.W):
                        if i == 0:
                            self.S[i][j] = self.LL[i][j]
                        else:
                            self.S[i][j] = self.S[i-1][j] + self.LL[i][j]
                #タテに累積和
                for i in range(self.H):
                    for j in range(self.W):
                        if j == 0:
                            self.S[i][j] = self.S[i][j]
                        else:
                            self.S[i][j] = self.S[i][j-1] + self.S[i][j]
            else:
                # 累積和(DPで算出)
                # 0行目/0列目に0を挿入した二次元累積和Sを得る。
                self.S = [[0] * (self.W + 1) for _ in range(self.H + 1)]
                for i in range(self.H):
                    for j in range(self.W):
                        self.S[i + 1][j + 1] = self.S[i + 1][j] + self.S[i][j + 1] - self.S[i][j] + self.LL[i][j]
            return
        
        def getArea(self, excY, incY, excX, incX) -> int:
            '''
            exampl) excX = 1, excY = 0, incX = 3, incY = 2
                    excX  incX
                    0  1  2  3
            excY 0  x  x  x  x
                 1  x  x  o  o
            incY 2  x  x  o  o
            '''
            areaAccumulate = self.S[incY][incX] - self.S[excY][incX] - self.S[incY][excX] + self.S[excY][excX]
            return areaAccumulate
        
        def printS(self) -> int:
            for i in range(self.H):
                print(self.S[i])
            return
        
    M = 5000 + 1
    ma = MatrixAccumulates(M, M)
    for aa, bb in zip(A, B):
        ma.add(aa, bb, 1)
    ma.build(1)
    ans = 0
    for aa in range(M):
        for bb in range(M):
            al = 0 if aa == 0 else aa - 1
            bl = 0 if bb == 0 else bb - 1
            ak = aa + K if aa + K < M else M - 1
            bk = bb + K if bb + K < M else M - 1
            p = ma.getArea(al, ak, bl, bk)
            ans = max(ans, p)
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
    K = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, K, A, B)

if __name__ == '__main__':
    main()
