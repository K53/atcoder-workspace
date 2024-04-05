#!/usr/bin/env python3
from collections import deque
class DoublyLinkedList():
    def __init__(self, init_list: list = [], inf: int = 10 ** 12) -> None:
        self.INF = inf
        self.HEAD = -inf
        self.TAIL = inf
        self.heads = {}
        self.tails = {}
        self.original = [self.HEAD] + init_list + [self.TAIL]
        # self.top = self.HEAD
        
        for i in range(len(self.original)):
            head_of_target = self.original[i - 1] if i - 1 >= 0 else None
            target = self.original[i]
            tail_of_target = self.original[i + 1] if i + 1 < len(self.original) else None
            self.heads[target] = head_of_target
            self.tails[target] = tail_of_target
        return
    
    # 速度面から直接fronts / backs にアクセスせよ。
    # def get_front(self, x: int) -> int:
    #     return self.heads[x]

    # def get_back(self, x: int) -> int:
    #     return self.tails[x]

    def add(self, val: int, head: int = None, tail: int = None) -> None:
        self.heads[val] = head if head != None else self.HEAD
        self.tails[val] = tail if tail != None else self.TAIL
        return
    
    def insert_front(self, x: int, val: int):
        """
        要素xの前に挿入
        """
        if x not in self.heads.keys():
            raise Exception(f"{x} is not in the list")
        head_of_x = self.heads[x]
        self.heads[x] = val
        self.tails[head_of_x] = val
        self.heads[val] = head_of_x
        self.tails[val] = x

    def insert_back(self, x: int, val: int):
        """
        要素xの前に挿入
        """
        if x not in self.heads.keys():
            raise Exception(f"{x} is not in the list")
        tail_of_x = self.tails[x]
        self.heads[tail_of_x] = val
        self.tails[x] = val
        self.heads[val] = x
        self.tails[val] = tail_of_x

    def delete(self, x: int):
        """
        要素xを削除
        """
        if x not in self.heads.keys():
            raise Exception(f"{x} is not in the list")
        head_of_x = self.heads[x]
        tail_of_x = self.tails[x]
        self.heads[tail_of_x] = head_of_x
        self.tails[head_of_x] = tail_of_x
        del self.heads[x]
        del self.tails[x]

    def get_actual_list(self, x: int = None) -> list:
        actual_list = deque()
        next = x if x != None else self.tails[self.HEAD]
        while next != self.TAIL:
            actual_list.append(next)
            next = self.tails[next]
        return actual_list

    def __str__(self) -> str:
        return " ".join(map(str, self.get_actual_list()))
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    nums = set(A)
    for _ in range(Q):
        l = list(map(int, input().split()))
        queries.append(l)
        if l[0] == 1:
            nums.add(l[2])

    raw_to_compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(nums))):
        raw_to_compressed[val] = index
        compressed_to_raw.append(val)
    
    A_cp = [raw_to_compressed[aa] for aa in A]
    dll = DoublyLinkedList(A_cp)
    queries_cp = []
    for qq in queries:
        if qq[0] == 1:
            queries_cp.append((qq[0], raw_to_compressed[qq[1]], raw_to_compressed[qq[2]]))
        else:
            queries_cp.append((qq[0], raw_to_compressed[qq[1]]))

    for qq in queries_cp:
        if qq[0] == 1:
            x, y = qq[1], qq[2]
            dll.insert_back(x, y)
        else: 
            x = qq[1]
            dll.delete(x)

    print(*[compressed_to_raw[num] for num in dll.get_actual_list()])
    return

if __name__ == '__main__':
    main()
