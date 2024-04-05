import sys
sys.path.append("../")
sys.path.append("../../")
from generateRandomInput import RangeCondition, PairCondition, QueryCondition, genRandInt, genRandQueries, writeNums, writeLists

def genFileName():
    i = 1
    while True:
        yield f"test{i}.txt"
        i += 1

def main():
    gfName = genFileName()

    """
    ■ 条件
    1 ≦ Q ≦ 20
    各クエリは以下のいずれか
    - (1, x, y) 
    - (2, x)
    1種類目のクエリにおいて 1 ≦ x, y ≦ 10 
    2種類目のクエリにおいて 1 ≦ x ≦ 100
    2種類目のクエリは少なくとも1回与えられる。
    ------------------
    ■ 入力形式
    Q
    query^1
    query^2
    :
    query^Q
    """
    with open(gfName.__next__(), "w") as handler:
        q1 = genRandInt(0, 10)
        q2 = genRandInt(1, 10)
        Q = q1 + q2
        query1_pairCondition = PairCondition(
            rangeConditions=[
            RangeCondition(
                valiable_name="x",
                integer_min_val=1,
                integer_max_val=10
            ), RangeCondition(
                valiable_name="y",
                integer_min_val=1,
                integer_max_val=10
            )],
            length=q1
        )
        query2_pairCondition = PairCondition(
            rangeConditions=[
            RangeCondition(
                valiable_name="x",
                integer_min_val=1,
                integer_max_val=100
            )],
            length=q2
        )
        query1_condition = QueryCondition(
            query_name="1",
            pairCondition=query1_pairCondition
        )
        query2_condition = QueryCondition(
            query_name="2",
            pairCondition=query2_pairCondition
        )
        l = genRandQueries(queryConditions=[query1_condition, query2_condition])
        writeNums(handler, Q)
        writeLists(handler, l, vertical=True)

    """
    ■ 条件
    1 ≦ N ≦ 10
    1 ≦ Q ≦ 20
    各クエリは以下のいずれか
    - (1, C, p) 
    - (2, p)
    1種類目のクエリにおいて C は "R", "L", "U", "D" のいずれか。
    2種類目のクエリは少なくとも1回与えられる。
    各クエリにおいて 1 ≦ p ≦ N
    ------------------
    ■ 入力形式
    N Q
    query^1
    query^2
    :
    query^Q
    """
    with open(gfName.__next__(), "w") as handler:
        N = genRandInt(1, 10)
        q1 = genRandInt(0, 10)
        q2 = genRandInt(1, 10)
        Q = q1 + q2
        query1_pairCondition = PairCondition(
            rangeConditions=[
            RangeCondition(
                valiable_name="C",
                select_candidates=["R", "L", "U", "D"]
            ), RangeCondition(
                valiable_name="p",
                integer_min_val=1,
                integer_max_val=N
            )],
            length=q1
        )
        query2_pairCondition = PairCondition(
            rangeConditions=[
            RangeCondition(
                valiable_name="p",
                integer_min_val=1,
                integer_max_val=N
            )],
            length=q2
        )
        query1_condition = QueryCondition(
            query_name="1",
            pairCondition=query1_pairCondition
        )
        query2_condition = QueryCondition(
            query_name="2",
            pairCondition=query2_pairCondition
        )
        l = genRandQueries(queryConditions=[query1_condition, query2_condition])
        writeNums(handler, N, Q)
        writeLists(handler, l, vertical=True)

    """
    ■ 条件
    1 ≦ Q ≦ 20
    各クエリは以下のいずれか
    - (1, L, R) 
    - (2, x)
    1種類目のクエリにおいて 1 ≦ L < R ≦ 10 
    2種類目のクエリにおいて 1 ≦ x ≦ 100
    ------------------
    ■ 入力形式
    Q
    query^1
    query^2
    :
    query^Q
    """
    with open(gfName.__next__(), "w") as handler:
        q1 = genRandInt(0, 10)
        q2 = genRandInt(1, 10)
        Q = q1 + q2
        query1_pairCondition = PairCondition(
            rangeConditions=[
            RangeCondition(
                valiable_name="L",
                integer_min_val=1,
                integer_max_val=10
            ), RangeCondition(
                valiable_name="R",
                integer_min_val=1,
                integer_max_val=10
            )],
            length=q1
        )
        query2_pairCondition = PairCondition(
            rangeConditions=[
            RangeCondition(
                valiable_name="x",
                integer_min_val=1,
                integer_max_val=100
            )],
            length=q2
        )
        query1_condition = QueryCondition(
            query_name="1",
            pairCondition=query1_pairCondition
        )
        query2_condition = QueryCondition(
            query_name="2",
            pairCondition=query2_pairCondition
        )
        l = genRandQueries(queryConditions=[query1_condition, query2_condition])
        writeNums(handler, Q)
        writeLists(handler, l, vertical=True)


if __name__ == '__main__':
    main()