import sys
sys.path.append("../")
sys.path.append("../../")
from generateRandomInput import genRandInt, genRandIntList, genRandStr, selectRandElementList, writeNums, writeLists

def genFileName():
    i = 1
    while True:
        yield f"test{i}.txt"
        i += 1

def main():
    gfName = genFileName()

    """
    ■ 条件
    1 ≦ H, W ≦ 10
    1 ≦ A^(i,j) ≦ H * W
    ------------------
    ■ 入力形式
    H W
    A^(1,1) A^(1,2) ... A^(1,W)
    :
    A^(H,1) A^(H,2) ... A^(H,W)
    """
    with open(gfName.__next__(), "w") as handler:
        H = genRandInt(1, 10)
        W = genRandInt(1, 10)
        writeNums(handler, H, W)
        for _ in range(H):
            A = genRandIntList(0, 10, W)
            writeLists(handler, A)

    """
    ■ 条件
    1 ≦ H, W ≦ 10
    0 ≦ A^(i,j) ≦ 10
    (i,j) ≠ (i',j') なら A^(i,j) ≠ A^(i',j')
    ------------------
    ■ 入力形式
    H W
    A^(1,1) A^(1,2) ... A^(1,W)
    :
    A^(H,1) A^(H,2) ... A^(H,W)
    """
    with open(gfName.__next__(), "w") as handler:
        H = genRandInt(1, 10)
        W = genRandInt(1, 10)
        candidates = set(range(1, H * W + 1))
        writeNums(handler, H, W)
        for _ in range(H):
            A = selectRandElementList(
                source_list=list(candidates),
                length=W,
                eliminateDuplicatedElements=True,
            )
            writeLists(handler, A)
            candidates -= set(A)

    """
    ■ 条件
    1 ≦ H, W ≦ 10
    A^(i,j) は "+" または "-"
    ------------------
    ■ 入力形式
    H W
    A^(1,1)A^(1,2)...A^(1,W)
    :
    A^(H,1)A^(H,2)...A^(H,W)
    """
    with open(gfName.__next__(), "w") as handler:
        H = genRandInt(1, 10)
        W = genRandInt(1, 10)
        writeNums(handler, H, W)
        for _ in range(H):
            A = genRandStr(W, W, "-+")
            writeLists(handler, A, delimiter="")

    """
    ■ 条件
    1 ≦ H, W ≦ 8
    A^(i,j) は "." または "#"
    ------------------
    ■ 入力形式
    H W
    S^(1,1)S^(1,2)...S^(1,W)
    :
    S^(H,1)S^(H,2)...S^(H,W)
    """
    with open(gfName.__next__(), "w") as handler:
        H = genRandInt(1, 8)
        W = genRandInt(1, 8)
        writeNums(handler, H, W)
        for _ in range(H):
            S = genRandStr(W, W, ".#")
            writeLists(handler, S, delimiter="")
        
    return

if __name__ == '__main__':
    main()
