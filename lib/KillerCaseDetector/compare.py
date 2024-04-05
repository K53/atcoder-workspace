#!/usr/bin/env python3
import sys

def main():
    args = sys.argv
    _, out_expected_1, out_actual_1 = args[0], args[1], args[2]
    with open(out_expected_1) as greedy_1, open(out_actual_1) as target_1:
        lines_greedy_1 = list(map(lambda l: l.rstrip("\n"), greedy_1.readlines()))
        lines_target_1 = list(map(lambda l: l.rstrip("\n"), target_1.readlines()))
        if lines_greedy_1 != lines_target_1:
            for greedy, target in zip(lines_greedy_1, lines_target_1):
                if greedy == target:
                    print(greedy, target)
                assert greedy == target, f"Expected : {greedy} != Actual : {target}"

if __name__ == '__main__':
    main()
