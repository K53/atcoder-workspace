# ------------------------------------------------------------------------------
#     Binary Index Tree (BIT / フェネック木)
# ------------------------------------------------------------------------------
# 解説
# - 
# 
# 考察
# - 
# 
# リンク
# - https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree (イメージ)
# - https://algo-logic.info/binary-indexed-tree/ (実装)
# - https://scrapbox.io/pocala-kyopro/%E8%BB%A2%E5%80%92%E6%95%B0 (転倒数)
# 
# 計算量
# - 
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=jp
# ------------------------------------------------------------------------------
class BIT:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (self.N + 1) # 1-indexedのため
        
    def add(self, pos, val):
        '''Add : A[pos] = val '''
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.tree[i] += val
            i += i & -i

    def sum(self, pos):
        ''' Return Sum(A[1], ... , A[pos])'''
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.tree[i]
            # res %= MOD
            i -= i & -i    
        return res
    
    def lower_bound(self, x):
    # 累積和がx以上になる最小のindexと、その直前までの累積和
        pass


# 転倒数
l = [3, 0, 5, 4, 2]
bit = BIT(6)
ans = 0

# 既出のもの(=自分より左側のもの)からBITに記入されることを利用している。
# 大小比較のIFとかがないのもその理由。
for i in range(len(l)):
    val = l[i]
    print(bit.tree[1:])
    print(val, ":",  bit.sum(val)) # 今の位置iよりも左側に、今の位置の数valよりも大きい数は何個あるか。
    ans += i - bit.sum(val) 
    bit.add(val, 1)

print(bit.tree[1:])
print(ans)


