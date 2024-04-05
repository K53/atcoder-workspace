import sys
sys.path.append("../")
sys.path.append("../../")
from generateRandomInput import RangeCondition, PairCondition, genRandInt, genRandPrime, genRandStr, genRandValPairsWithConditions, selectRandElement, writeNums

def genFileName():
    i = 1
    while True:
        yield f"test{i}.txt"
        i += 1

def main():
    gfName = genFileName()
    
    """
    ■ 条件
    0 ≦ N ≦ 10
    |M| ≦ 10
    2 ≦ P ≦ 1000
    Pは素数
    ------------------
    ■ 入力形式
    N
    M
    P
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(0, 10)
        M = genRandInt(-10, 10)
        P = genRandPrime(0, 100)
        writeNums(handler, N)
        writeNums(handler, M)
        writeNums(handler, P)

    """
    ■ 条件
    |S|, |T| ≦ 10
    文字列S は "0", "1", "?" のいずれか。
    文字列T は 英小文字。
    ------------------
    ■ 入力形式
    S
    T
    """
    with open(gfName.__next__(), "w") as handler:
        S = genRandStr(10, 10, ["0", "1", "?"])
        T = genRandStr(10, 10)
        writeNums(handler, S)
        writeNums(handler, T)

    """
    ■ 条件
    x, yは0,1,2のいずれか
    0 ≦ L < R ≦ 10
    ------------------
    ■ 入力形式
    x y
    L R
    """
    with open(gfName.__next__(), "w") as handler:
        x = selectRandElement(source_list=[0,1,2])
        y = selectRandElement(source_list=[0,1,2])
        L_rangeCondition = RangeCondition(
            valiable_name="L",
            integer_min_val=0,
            integer_max_val=10,
        )
        R_rangeCondition = RangeCondition(
            valiable_name="R",
            integer_min_val=0,
            integer_max_val=10,
        )
        LRs_pairCondition = PairCondition(
            rangeConditions=[L_rangeCondition, R_rangeCondition],
            length=1, 
            eliminateUnsortedPair=True,
            eliminateAllSameElementsPair=True,
        )
        LRs = genRandValPairsWithConditions(
            pairCondition=LRs_pairCondition
        )
        L = LRs["L"][0]
        R = LRs["R"][0]
        writeNums(handler, x, y)
        writeNums(handler, L, R)

if __name__ == '__main__':
    main()
