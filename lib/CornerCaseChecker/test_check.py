import sys
import os
import pytest
from greedy import solve as greedy_solve
from main import solve as main_solve
import random
import time

# 実行
# python -m pytest -s
checkTimes = 10 # テスト試行回数
D5 = 10 ** 5
D6 = 10 ** 6
D7 = 10 ** 7
D8 = 10 ** 8
D9 = 10 ** 9

def getRandomValueOnce(min_val: int, max_val: int):
    if min_val > max_val:
        raise Exception(f"min_val ({min_val}) > max_val ({max_val})")
    return random.randint(min_val, max_val)

def getRandomValuesList(min_val: int, max_val: int, length: int):
    if min_val > max_val:
        raise Exception(f"min_val ({min_val}) > max_val ({max_val})")
    return [random.randint(min_val, max_val) for _ in range(length)]

def testNomalCase1(capfd):
    def _check(*args):
        _, _ = capfd.readouterr() # Flash stdout  # 正常なテストケースは出力されない。
        greedy_solve(*args)
        greedy_output, greedy_err = capfd.readouterr()
        begin_main_time = time.time()
        main_solve(*args)
        end_main_time = time.time()
        main_output, main_err = capfd.readouterr()
        print()
        print("------  TIME  ------")
        print(end_main_time - begin_main_time, "[sec]")
        print("------ TESTED ------")
        print(*args)
        print()
        assert greedy_output == main_output
        assert greedy_err == main_err

    for _ in range(checkTimes):
        N = getRandomValueOnce(1, 1)
        # K = getRandomValueOnce(0, N)
        # H = getRandomValuesList(1, D9, N)
        _check(N)
