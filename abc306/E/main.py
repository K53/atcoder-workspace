#!/usr/bin/env python3
import sys
import bisect

INF = 10 ** 9

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (self.N + 1) # 1-indexedのため
        
    def add(self, pos, val):
        '''Add
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            A[pos] += val 
        '''
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] += val
            i += i & -i

    def deleteNonNegative(self, pos, val) -> int:
        '''Add
            O(logN)
            ※ multisetで使用される関数
            posは0-index。内部で1-indexedに変換される。
            すでにMultiSetに含まれている個数以上は削除されない。
            A[pos] -= val 
        '''
        actualSubstractVal = min(val, self.sum(pos) - self.sum(pos - 1)) # pos - 1は負になってもself.sum()は大丈夫
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] -= actualSubstractVal
            i += i & -i
        return actualSubstractVal

    def sum(self, pos):
        ''' Sum
            0からposまでの和を返す(posを含む)
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            Return Sum(A[0], ... , A[pos])
            posに負の値を指定されるとSum()すなわち0を返すのでマイナスの特段の考慮不要。
        '''
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.bit[i]
            i -= i & -i    
        return res
    
    def lowerLeft(self, w):
        '''
        O(logN)
        A0 ~ Aiの和がw以上となる最小のindex(値)を返す。
        Ai ≧ 0であること。
        '''
        if (w < 0):
            return 0
        total = self.sum(self.N - 1)
        if w > total:
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x
        
    def __str__(self):
        '''
        index0は不使用なので表示しない。
        '''
        return "[" + ", ".join(f'{v}' for v in self.bit[1:]) + "]"
    
class MultiSet:
    def __init__(self, allVals: "list[int]"):
        self.arr = sorted(allVals)
        self.bit = BIT(len(allVals))
        self.ammounts = 0
        
    def insert(self, val: int, count: int = 1):
        idx = bisect.bisect_left(self.arr, val)
        self.bit.add(idx, count)
        self.ammounts += count
    
    def delete(self, val: int, count : int = 1):
        k = bisect.bisect_left(self.arr, val)
        self.bit.add(k, -count)
        self.ammounts -= count
    
    def deleteIgnoreOverSubstract(self, val: int, count : int = 1):
        '''
        MultiSetで保持している個数以上の削除を求められたら無視する。
        '''
        k = bisect.bisect_left(self.arr, val)
        actualSubstractVal = self.bit.deleteNonNegative(k, count)
        self.ammounts -= actualSubstractVal
    
    def getKth(self, k: int) -> int:
        '''getKth
        k : 0-indexed
        小さい方からK番目の値を取得。
        '''
        return self.arr[self.bit.lowerLeft(k + 1)] if 0 <= k < self.ammounts else -INF

    def getKthFromLargest(self, k: int) -> int:
        '''getKth
        k : 0-indexed
        大きい方からK番目の値を取得。
        '''
        return self.arr[self.bit.lowerLeft(self.ammounts - k)] if 0 <= k < self.ammounts else -INF
        
    def countLessThanOrEqualTo(self, val: int) -> int:
        '''
        val以下(≦ val)の要素数を返す。
        '''
        return 0 if val < self.arr[0] else self.bit.sum(bisect.bisect_left(self.arr, val))
    
    def countUnder(self, val: int) -> int:
        '''
        val未満(< val)の要素数を返す。
        '''
        return 0 if val < self.arr[0] else self.bit.sum(bisect.bisect_left(self.arr, val) - 1) # sum()は負なら0が返るのでvalがarrの最下端の数字でもOK

    def upperBound(self, val: int, k: int) -> int:
        '''upperBound
        | - - - -|-|< - - ->|
                 l u
        valより大きい値において、小さい方からk番目の値を取得
        k: 0-indexed
        (存在しないindexでは-INFが返る。)
        '''
        return self.getKth(self.countLessThanOrEqualTo(val) + k)

    def lowerBound(self, val: int, k: int) -> int:
        '''upperBound
        | - - - -|<-| - - ->|
                 l  u
        val以上の値において、小さい方からk番目の値を取得
        k: 0-indexed
        (存在しないindexでは-INFが返る。)
        '''
        return self.getKth(self.countUnder(val) + k)

    def __str__(self):
        res = []
        for i in range(len(self.arr)):
            count = self.bit.sum(i) - (self.bit.sum(i - 1) if i - 1 >= 0 else 0)
            for _ in range(count):
                res.append(i)
        return "[" + ", ".join(f'{self.arr[v]}' for v in res) + "]"

def solve(N: int, K: int, Q: int, X: "List[int]", Y: "List[int]"):
    raw_to_compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(set(Y + [0])))):
        raw_to_compressed[val] = index
        compressed_to_raw.append(val)
    # print(raw_to_compressed)
    # print(compressed_to_raw)
    curA = [0] * N

    tree = MultiSet(raw_to_compressed.values())
    tree.insert(0, N)
    sumNum = 0
    for i in range(Q):
        xx, yy = X[i] - 1, raw_to_compressed[Y[i]]

        # 消される < K
        # print(xx, curA[xx], tree.getKthFromLargest(K - 1), i)
        if curA[xx] >= tree.getKthFromLargest(K - 1):
            sumNum -= compressed_to_raw[curA[xx]]
            # print(sumNum, "$2")
        # 消されない
        else:
            sumNum -= compressed_to_raw[tree.getKthFromLargest(K - 1)]
            # print(sumNum, "$")
        # 共通
        tree.delete(curA[xx], 1)
        # 挿入
        # print(yy, K, tree.lowerBound(yy, K - 1), i)
        if tree.lowerBound(yy, K - 1) == -INF:
            # 挿入は影響する
            sumNum += Y[i]
        else:
            # 挿入は影響しない -> 次のやつを入れる
            sumNum += compressed_to_raw[tree.getKthFromLargest(K - 1)]
        tree.insert(yy, 1)
        curA[xx] = yy
        print(sumNum)


        
        # else: # 影響しない
            # print(sumNum)
            # # 削除
            # target = tree.getKth(xx)
            # if target != -INF:
            #     tree.delete(target, 1)
            # tree.insert(yy, 1)
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
    Q = int(next(tokens))  # type: int
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, K, Q, X, Y)

if __name__ == '__main__':
    main()
