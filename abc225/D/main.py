#!/usr/bin/env python3
from collections import deque
class DoublyLinkedList():
    def __init__(self, init_list: list = [], inf: int = 10 ** 12) -> None:
        self.HEAD = -inf
        self.TAIL = inf
        self.heads = {}
        self.tails = {}
        self.original = [self.HEAD] + init_list + [self.TAIL]
        
        for i in range(len(self.original)):
            head_of_target = self.original[i - 1] if i - 1 >= 0 else None
            target = self.original[i]
            tail_of_target = self.original[i + 1] if i + 1 < len(self.original) else None
            self.heads[target] = head_of_target
            self.tails[target] = tail_of_target
        return
    
    def add(self, val: int, head: int = None, tail: int = None) -> None:
        if head == None: head = self.HEAD
        if tail == None: tail = self.TAIL
        self.heads[val] = head
        self.tails[val] = tail
        return
    
    def insert_front(self, x: int, val: int):
        """
        要素xの前にvalを挿入
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
        要素xの前にvalを挿入
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

    def link(self, x: int, y: int) -> None:
        """
        x -> yの向きに連結する。(xの後部とyの前部を連結する。)
        """
        if self.tails[x] != self.TAIL:
            raise Exception(f"Already Linked : tail of {x}")
        if self.heads[y] != self.HEAD:
            raise Exception(f"Already Linked : head of {y}")
        self.heads[y] = x
        self.tails[x] = y
        return

    def unlink(self, x: int, y: int) -> None:
        """
        x -> yの向きに連結を削除する。(xの後部とyの前部の連結を解除する。)
        """
        if self.tails[x] == self.TAIL:
            raise Exception(f"Not Linked : tail of {x}")
        if self.heads[y] == self.HEAD:
            raise Exception(f"Not Linked : head of {y}")
        self.heads[y] = self.HEAD
        self.tails[x] = self.TAIL
        return

    def get_actual_list(self, x: int) -> list:
        """
        要素xを含む一連のリストを出力する。
        """
        actual_list = deque([x])
        next = self.tails[x]
        while next != self.TAIL:
            actual_list.append(next)
            next = self.tails[next]
        prev = self.heads[x]
        while prev != self.HEAD:
            actual_list.appendleft(prev)
            prev = self.heads[prev]
        return actual_list

    # def __str__(self) -> str:
    #     return f"[{' '.join(map(str, self.get_actual_list()))}]"

def main():
    dll = DoublyLinkedList()
    N, Q = map(int, input().split())
    for i in range(N):
        dll.add(i + 1)
    for _ in range(Q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            x, y = l[1], l[2]
            dll.link(x, y)
        elif l[0] == 2:
            x, y = l[1], l[2]
            dll.unlink(x, y)
        else:
            x = l[1]
            ans = list(dll.get_actual_list(x))
            print(len(ans), *ans)

if __name__ == '__main__':
    main()
