# ------------------------------------------------------------------------------
#     Doubly Linked List (双方向連結リスト)
# ------------------------------------------------------------------------------
# 
# 条件
# - 各要素について重複がないこと。
# - インデックスに対する操作がないこと。 (前からi番目にxxxをするのようなクエリは不向き。)
#
# 関数
# - insert_front(x, val) : 要素xの前にvalを挿入する。要素xが存在しない場合は例外を返す。
# - insert_back(x, val) : 要素xの後ろにvalを挿入する。要素xが存在しない場合は例外を返す。
# - delete(x) : 要素xを削除する。要素xが存在しない場合は例外を返す。
# - get_actual_list() : 先頭から全ての要素を順にリストで返す。
# - get_front(x) : 要素xの前の要素を返す。
# - get_back(x) : 要素xの後の要素を返す。
#
# 検証
# - https://atcoder.jp/contests/abc344/tasks/abc344_e
# ------------------------------------------------------------------------------

class DoublyLinkedList():
    def __init__(self, init_list: list = [], inf: int = 10 ** 12) -> None:
        self.INF = inf
        self.fronts = {
            -self.INF: None,
            self.INF: -self.INF,
        }
        self.backs = {
            -self.INF: self.INF,
            self.INF: None,
        }
        self.original = [-self.INF] + init_list + [self.INF]
        self.top = -self.INF
        
        for i in range(len(self.original)):
            front_of_target = self.original[i - 1] if i - 1 >= 0 else None
            target = self.original[i]
            back_of_target = self.original[i + 1] if i + 1 < len(self.original) else None
            self.fronts[target] = front_of_target
            self.backs[target] = back_of_target
        return
    
    # 速度面から直接fronts / backs にアクセスせよ。
    # def get_front(self, x: int) -> int:
    #     return self.fronts[x]

    # def get_back(self, x: int) -> int:
    #     return self.backs[x]
    
    def insert_front(self, x: int, val: int):
        """
        要素xの前に挿入
        """
        if x not in self.fronts.keys():
            raise Exception(f"{x} is not in the list")
        front_of_x = self.fronts[x]
        self.fronts[x] = val
        self.backs[front_of_x] = val
        self.fronts[val] = front_of_x
        self.backs[val] = x

    def insert_back(self, x: int, val: int):
        """
        要素xの前に挿入
        """
        if x not in self.fronts.keys():
            raise Exception(f"{x} is not in the list")
        back_of_x = self.backs[x]
        self.fronts[back_of_x] = val
        self.backs[x] = val
        self.fronts[val] = x
        self.backs[val] = back_of_x

    def delete(self, x: int):
        """
        要素xを削除
        """
        if x not in self.fronts.keys():
            raise Exception(f"{x} is not in the list")
        front_of_x = self.fronts[x]
        back_of_x = self.backs[x]
        self.fronts[back_of_x] = front_of_x
        self.backs[front_of_x] = back_of_x
        del self.fronts[x]
        del self.backs[x]

    def get_actual_list(self) -> list:
        actual_list = []
        next = self.backs[self.top]
        while next != self.INF:
            actual_list.append(next)
            next = self.backs[next]
        return actual_list

    def __str__(self) -> str:
        return " ".join(map(str, self.get_actual_list()))



### 
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
