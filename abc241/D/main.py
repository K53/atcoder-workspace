#!/usr/bin/env python3

from collections import defaultdict
import re


class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(None, 1<<n)

    def append(self, v):# v を追加（その時点で v はない前提）
        print(v, "$1")
        v += 1
        nd = self.root
        if not nd.value:
            nd.value = v
            return
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
                        print(v, "$")
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                        print(v, "#")
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

    def upper_bound(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if not nd.value:
            return -1
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

    def lower_bound(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        # print(nd.value, v)
        if not nd.value:
            return -1
        if nd.value > v: prev = nd.value
        # print("!", prev)
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    # print("#", v, nd.value)
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    # print("-", v, nd.value)
                    return prev - 1

    # @property
    # def max(self):
    #     return self.upper_bound((1<<self.N)-1)

    # @property
    # def min(self):
    #     return self.lower_bound(-1)

    # def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
    #     v += 1
    #     if not nd: nd = self.root
    #     if not prev: prev = nd
    #     while v != nd.value:
    #         prev = nd
    #         if v <= nd.value:
    #             if nd.left:
    #                 nd = nd.left
    #             else:
    #                 #####
    #                 return
    #         else:
    #             if nd.right:
    #                 nd = nd.right
    #             else:
    #                 #####
    #                 return
    #     if (not nd.left) and (not nd.right):
    #         if not prev.left:
    #             prev.right = None
    #         elif not prev.right:
    #             prev.left = None
    #         else:
    #             if nd.pivot == prev.left.pivot:
    #                 prev.left = None
    #             else:
    #                 prev.right = None

    #     elif nd.right:
    #         # print("type A", v)
    #         nd.value = self.leftmost(nd.right).value
    #         self.delete(nd.value - 1, nd.right, nd)    
    #     else:
    #         # print("type B", v)
    #         nd.value = self.rightmost(nd.left).value
    #         self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.lower_bound(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    # def debug(self):
    #     def debug_info(nd_):
    #         return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

    #     def debug_node(nd):
    #         re = []
    #         if nd.left:
    #             re += debug_node(nd.left)
    #         if nd.value: re.append(debug_info(nd))
    #         if nd.right:
    #             re += debug_node(nd.right)
    #         return re
    #     print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    # def debug_list(self):
    #     def debug_node(nd):
    #         re = []
    #         if nd.left:
    #             re += debug_node(nd.left)
    #         if nd.value: re.append(nd.value - 1)
    #         if nd.right:
    #             re += debug_node(nd.right)
    #         return re
    #     return debug_node(self.root)[:-1]

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    Q = int(input())
    BT = BalancingTree(18)
    # d = defaultdict(int)
    for _ in range(10 ** 3):
        qq = list(map(int, input().split()))
        if qq[0] == 1:
            x = qq[1]
            # d[x] += 1
            # x = x * 10 ** 6 + d[x]
            BT.append(x)
        # elif qq[0] == 2:
        #     # BT.debug()
        #     res = qq[1]# * 10 ** 6
        #     for kk in range(qq[2]):
        #         res = BT.upper_bound(res)
        #         # print(res)
        #     print(res)
        #     # print(res // 10 ** 6)
        else:
            # BT.debug()
            res = qq[1]# * 10 ** 6 
            # for kk in range(qq[2]):
            #     res = BT.lower_bound(res)
            #     # print(res)
            print(res)
            # print(res // 10 ** 6)
    return

if __name__ == '__main__':
    main()
