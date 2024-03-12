#!/usr/bin/env python3
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
    
    def get_front(self, x: int):
        return self.fronts[x]

    def get_back(self, x: int):
        return self.backs[x]
    
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
