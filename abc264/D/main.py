#!/usr/bin/env python3
import sys

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
            posは0-index。内部で1-indexedに変換される。
            A[pos] += val 
        '''
        actualSubstractVal = min(val, self.sum(pos) - self.sum(pos - 1)) # pos - 1は負になってもself.sum()は大丈夫
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] -= actualSubstractVal
            i += i & -i
        return actualSubstractVal

    def sum(self, pos):
        ''' Sum
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
    

def solve(S: str):
    l = []
    for ss in S:
        l.append("atcoder".index(ss))
    
    bit = BIT(max(l) + 1)
    ans = 0

    # 既出のもの(=自分より左側のもの)からBITに記入されることを利用している。
    # 大小比較のIFとかがないのもその理由。
    for i in range(len(l)):
        val = l[i]
        # print(bit.bit[1:])
        # print(val, ":",  bit.sum(val)) # 今の位置iよりも左側に、今の位置の数valよりも大きい数は何個あるか。
        ans += i - bit.sum(val) 
        bit.add(val, 1)

    # print(bit.bit[1:])
    print(ans)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()