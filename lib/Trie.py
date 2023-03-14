
# https://algo-logic.info/trie-tree/
# https://note.com/omotiti/n/n689904103628

# verify予定
# https://atcoder.jp/contests/abc287/tasks/abc287_e

class Node:
    def __init__(self):
        self.children: dict = {}
        self.end: bool = False
        self.common: int = 0
        
    def __str__(self):
        node = self
        ret = "{ "
        for c in node.children:
            ret += str(c) + "(" + str(node.children[c].common) + ")" + ":" + str(node.children[c])
        ret += "} "
        return ret
       
class Trie:
    def __init__(self):
        self.root: Node = Node()
        self.nodes_count: int = 0 # rootノードを除く
       
    def add(self, word: str):
        """
        単語の追加
        O(|word|)
        """
        node = self.root
        node.common += 1
        for ch in word:
            if not ch in node.children:
                node.children[ch] = Node()
                self.nodes_count += 1
            node = node.children[ch]
            node.common += 1
        node.end = True
       
    def isPrefix(self, prefix: str):
        """
        prefixに一致する文字列が存在するか。
        O(|prefix|)
        """
        node = self.root
        for ch in prefix:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return True

    def getNumOfCommonPrefix(self, prefix: str):
        """
        prefixに一致する文字列がいくつ存在するか。
        O(|prefix|)
        """
        node = self.root
        for ch in prefix:
            if not ch in node.children:
                return 0
            node = node.children[ch]
        return node.common

    def search(self, word: str):
        """
        wordに一致する単語が存在するか。
        O(|word|)
        """
        node = self.root
        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        if node.end:
            return True
        else:
            return False
           
    def __str__(self):
        return str(self.root)

t = Trie()
t.add("fire")
t.add("fireman")
t.add("file")
t.add("directory")
print(t)
# { f(3):{ i(3):{ r(2):{ e(2):{ m(1):{ a(1):{ n(1):{ } } } } } l(1):{ e(1):{ } } } } d(1):{ i(1):{ r(1):{ e(1):{ c(1):{ t(1):{ o(1):{ r(1):{ y(1):{ } } } } } } } } } } 
print(t.nodes_count) # ノードの個数 18
print(t.isPrefix("fir")) # プレフィックスが存在するか True
print(t.getNumOfCommonPrefix("fire"))   # 2
print(t.getNumOfCommonPrefix("fil"))    # 1
print(t.getNumOfCommonPrefix("fi"))     # 3
print(t.getNumOfCommonPrefix("k"))      # 0