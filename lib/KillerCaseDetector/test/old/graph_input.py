import sys
sys.path.append("../")
sys.path.append("../../")
from generateRandomInput import RangeCondition, PairCondition, genRandInt, genRandValPairsWithConditions, writeNums, writeLists

def genFileName():
    i = 1
    while True:
        yield f"test{i}.txt"
        i += 1

def main():
    gfName = genFileName()
    """
    ■ 条件 : 配列の組み合わせにおけるペアの重複排除、ペア内の値の不等号
    2 ≦ N ≦ 10 (ノード数)
    0 ≦ M ≦ N(N - 1)/2 (エッジ数)
    0 ≦ U^i < V^i ≦ N
    i ≠ j なら (U^i, V^i) ≠ (U^j, V^j)
    ------------------
    ■ 入力形式
    N M
    U^1 V^1
    U^2 V^2
    :
    U^M V^M
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(2, 10)
        M = genRandInt(0, N * (N - 1) // 2)
        U_rangeCondition = RangeCondition(
            valiable_name="U",
            integer_min_val=1,
            integer_max_val=N,
        )
        V_rangeCondition = RangeCondition(
            valiable_name="V",
            integer_min_val=1,
            integer_max_val=N,
        )
        UVs_pairCondition = PairCondition(
            rangeConditions=[U_rangeCondition, V_rangeCondition],
            length=M, 
            eliminateDuplicatedPair=True,
            eliminateUnsortedPair=True,
            eliminateAllSameElementsPair=True,
        )
        UVs = genRandValPairsWithConditions(
            pairCondition=UVs_pairCondition,
        )
        U = UVs["U"]
        V = UVs["V"]
        writeNums(handler, N, M)
        writeLists(handler, U, V, vertical=True)

    """
    ■ 条件 : 配列の組み合わせにおけるペアの重複排除、ペア内の値の不等号、連結グラフ
    2 ≦ N ≦ 1000
    N - 1 ≦ M ≦ 1000
    0 ≦ U^i < V^i ≦ N
    i ≠ j なら (U^i, V^i) ≠ (U^j, V^j)
    グラフは連結
    ------------------
    ■ 入力形式
    N M
    U^1 V^1
    U^2 V^2
    :
    U^M V^M
    """
    # TODO


if __name__ == '__main__':
    main()
