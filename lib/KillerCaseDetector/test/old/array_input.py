import sys
import string
sys.path.append("../")
sys.path.append("../../")
from generateRandomInput import RangeCondition, PairCondition, genRandInt, genRandIntList, genRandStrList, genRandValPairsWithConditions, writeNums, writeLists

def genFileName():
    i = 1
    while True:
        yield f"test{i}.txt"
        i += 1

def main():
    gfName = genFileName()
    """
    ■ 条件
    1 ≦ N, M ≦ 10
    0 ≦ A^i, B^i, C^i, D^i ≦ 10
    ------------------
    ■ 入力形式
    N M
    A^1 A^2 ... A^N
    B^1 B^2 ... B^M
    C^1 D^1
    C^2 D^2
    :
    C^N D^N
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        M = genRandInt(1, 10)
        A = genRandIntList(0, 10, N)
        B = genRandIntList(0, 10, M)
        C = genRandIntList(0, 10, N)
        D = genRandIntList(0, 10, N)
        writeNums(handler, N, M)
        writeLists(handler, A, B)
        writeLists(handler, C, D, vertical=True)
    
    """
    ■ 条件 : 単一の配列における重複排除
    1 ≦ N ≦ 10
    1 ≦ A^i ≦ N
    1 ≦ B^i ≦ N
    A^i ≠ A^j
    B^i ≠ B^j
    ------------------
    ■ 入力形式
    N
    A^1 A^2 ... A^N
    B^1 B^2 ... B^N
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        # 方法1
        A = genRandIntList(1, N, N, eliminateDuplicatedElements=True)
        # 方法2
        # ---------------
        # NOT RECOMMENDED
        # genRandValPairsWithConditions()による配列生成は主にペアを生成する際に条件がある場合に使用する。
        # ---------------
        B_rangeCondition = RangeCondition(
            valiable_name="B",
            integer_min_val=1,
            integer_max_val=N,
            eliminateDuplicatedElements=True,
        )
        Bs_pairCondition = PairCondition(
            rangeConditions=[B_rangeCondition],
            length=N,
        )
        Bs = genRandValPairsWithConditions(
            pairCondition=Bs_pairCondition,
        )
        B = Bs["B"]
        writeNums(handler, N)
        writeLists(handler, A, B)
        

    """
    ■ 条件 : 配列の組み合わせにおける同値ペア排除
    0 ≦ N ≦ 10
    0 ≦ A^i, B^i ≦ 10
    A^i ≠ B^i
    ------------------
    ■ 入力形式
    N
    A^1 B^1
    A^2 B^2
    :
    A^N B^N
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(2, 10)
        A_rangeCondition = RangeCondition(
            valiable_name="A",
            integer_min_val=0,
            integer_max_val=10,
        )
        B_rangeCondition = RangeCondition(
            valiable_name="B",
            integer_min_val=0,
            integer_max_val=10,
        )
        ABs_pairCondition = PairCondition(
            rangeConditions=[A_rangeCondition, B_rangeCondition],
            length=N,
            eliminateAllSameElementsPair=True
        )
        ABs = genRandValPairsWithConditions(
            pairCondition=ABs_pairCondition,
        )
        A = ABs["A"]
        B = ABs["B"]
        writeNums(handler, N)
        writeLists(handler, A, B, vertical=True)

    """
    ■ 条件 : 単一の配列における重複排除
    1 ≦ N ≦ 10
    1 ≦ |S^i| ≦ 10
    1 ≦ T^i ≦ 100
    S^i ≠ S^j
    T^i ≠ T^j
    S^iは英小文字、英大文字、数字のみからなる
    ------------------
    ■ 入力形式
    N
    S^1 T^1
    S^2 T^2
    :
    S^N T^N
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        S_rangeCondition = RangeCondition(
            valiable_name="S",
            string_min_length=1,
            string_max_length=10,
            string_candidates=string.ascii_letters + "0123456789",
        )
        T_rangeCondition = RangeCondition(
            valiable_name="T",
            integer_min_val=1,
            integer_max_val=100,
        )
        STs_pairCondition = PairCondition(
            rangeConditions=[S_rangeCondition, T_rangeCondition],
            length=N,
        )
        STs = genRandValPairsWithConditions(
            pairCondition=STs_pairCondition,
        )
        S = STs["S"]
        T = STs["T"]
        writeNums(handler, N)
        writeLists(handler, S, T, vertical=True)
    
    """
    ■ 条件 : 単一の配列における重複排除
    1 ≦ N ≦ 10
    1 ≦ A^i ≦ C^i ≦ 100
    1 ≦ B^i < D^i ≦ 10
    B^i ≠ B^j
    ------------------
    ■ 入力形式
    N
    A^1 B^1 C^1 D^1
    A^2 B^2 C^2 D^2
    :
    A^N B^N C^N D^N
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        A_rangeCondition = RangeCondition(
            valiable_name="A",
            integer_min_val=1,
            integer_max_val=100,
        )
        C_rangeCondition = RangeCondition(
            valiable_name="C",
            integer_min_val=1,
            integer_max_val=100,
        )
        ACs_pairCondition = PairCondition(
            rangeConditions=[A_rangeCondition, C_rangeCondition],
            length=N,
            eliminateUnsortedPair=True,
        )
        ACs = genRandValPairsWithConditions(
            pairCondition=ACs_pairCondition,
        )
        B_rangeCondition = RangeCondition(
            valiable_name="B",
            integer_min_val=1,
            integer_max_val=10,
            eliminateDuplicatedElements=True,
        )
        D_rangeCondition = RangeCondition(
            valiable_name="D",
            integer_min_val=1,
            integer_max_val=10,
        )
        BDs_pairCondition = PairCondition(
            rangeConditions=[B_rangeCondition, D_rangeCondition],
            length=N,
            eliminateUnsortedPair=True,
            eliminateAllSameElementsPair=True,
        )
        BDs = genRandValPairsWithConditions(
            pairCondition=BDs_pairCondition,
        )
        A = ACs["A"]
        C = ACs["C"]
        B = BDs["B"]
        D = BDs["D"]
        writeNums(handler, N)
        writeLists(handler, A, B, C, D, vertical=True)
        
    """
    ■ 条件 : 単一の配列における重複排除
    1 ≦ N ≦ 10
    3 ≦ |s^i| ≦ 8
    S^iは英小文字、英大文字のみからなる
    ------------------
    ■ 入力形式
    N
    s^1
    s^2
    :
    s^N
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        s = genRandStrList(3, 8, string.ascii_letters, N)
        writeNums(handler, N)
        writeLists(handler, s, vertical=True)
    
    """
    ■ 条件 : 単一の配列における重複排除
    1 ≦ N ≦ 10
    1 ≦ A^i ≦ 10
    1 ≦ |S^(i,j)| ≦ 10
    S^iは英小文字のみからなる
    ------------------
    ■ 入力形式
    N
    A^1 S^(1,1) S^(1,2) ... S^(1,A^1)
    A^2 S^(2,1) S^(2,2) ... S^(2,A^2)
    :
    A^N S^(N,1) S^(N,2) ... S^(N,A^N)
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        writeNums(handler, N)
        for _ in range(N):
            Ai = genRandInt(1, 10)
            S = genRandStrList(1, 10, string.ascii_letters, Ai)
            writeLists(handler, [Ai] + S)
    
    return


if __name__ == '__main__':
    main()
