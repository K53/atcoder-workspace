

def greedy(N: int, K: int, S: list[int]):
    # 貪欲法コード
    pass

def solve(N: int, K: int, S: list[int]):
    # 提出コード
    pass

checkTimes = 10 # テスト試行回数
for i in range(checkTimes):
    import random
    N = 10
    K = random.randint(1, 4) # 発生させる乱数範囲 (末尾を含む)
    S = [random.randint(1, 10) for _ in range(10)]
    ac = greedy(N,K,S)
    checkee = solve(N,K,S)
    if ac != checkee:
        print(N, K)
        print(S)
        print(ac, "!=", checkee)
        print("----------------")