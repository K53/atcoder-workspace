#!/usr/bin/env python3
import sys
class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:   # 小さい値を左へ
                    nd.value = ma
                    if nd.left: # すでに左が埋まってるなら同じ処理を繰り返し
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)    
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]

# BT = BalancingTree(5) # 0 ～ 30 までの要素を入れられるピボット木
# BT.append(3)
# BT.append(20)
# BT.append(5)
# BT.append(10)
# # BT.append(13)
# # BT.append(8)
# # BT.debug()
# # BT.delete(20)
# BT.debug()
# print(BT.find_l(12)) # 10
# # print(BT.find_r(5)) # 8
# # print(BT.min) # 3
# # print(BT.max) # 13
# # print(3 in BT) # True
# # print(4 in BT) # False
# print(BT.debug_list())

def solve(N: int, M: int, K: int, A: "List[int]"):
    from collections import defaultdict, deque
    sA = sorted(A)
    d = defaultdict(deque)
    for i in range(N):
        d[sA[i]].append(i)
    print(d)
    mappedA = []
    for aa in A:
        num = d[aa].pop()
        mappedA.append(num)
    print(mappedA) # [2, 1, 3, 0, 4, 5]
        
    
    bt = BalancingTree(N)
    ini = sorted(mappedA[:M])
    S = 0
    maxSinK = [-1, -2]
    for i in range(M):
        bt.append(ini[i])
        if i < K:
            S += sA[ini[i]]
            if maxSinK[0] < ini[i]:
                maxSinK = [ini[i], maxSinK[0]]
            elif maxSinK[1] < ini[i]:
                maxSinK = [maxSinK[0], ini[i]]
    print(S)
    print(maxSinK, "実質")
    print(bt.debug_list())

    for i in range(M, N):
        print(i, mappedA[i], "#", i - M)
        bt.delete(mappedA[i - M])
        print(bt.debug_list())
        S -= sA[maxSinK[1]]
        print("ぬけ", S)
        if maxSinK[0] < mappedA[i - M]:
            maxSinK = [maxSinK[1], -1]
        elif maxSinK[1] < mappedA[i - M]:
            maxSinK = [maxSinK[0], -1]

        val = bt.find_l(mappedA[i])
        print(val)
        if val == maxSinK[0]: # mappedA[i]は計算される
            S += sA[val]
            print(S, "##")
            if maxSinK[0] < val:
                maxSinK = [maxSinK[1], -1]
            elif maxSinK[1] < val:
                maxSinK = [maxSinK[0], -1]
        else:
            val = bt.find_r(maxSinK[0])
            S += sA[val]
            print(S, "##s")
            if maxSinK[0] < val:
                maxSinK = [maxSinK[1], -1]
            elif maxSinK[1] < val:
                maxSinK = [maxSinK[0], -1]
        print(S, "l")
        
                


        
        

        

    # print(S)
    

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, K, A)

if __name__ == '__main__':
    main()
