#!/usr/bin/env python3
import sys
    
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2013

def main():
    def convert(hh, mm, ss):
        return (hh * 60 + mm) * 60 + ss
    
    while True:
        n = int(sys.stdin.readline())
        times = [0] * (24 * 3600 + 1)
        if n == 0:
            return
        for i in range(n):
            s = False
            for t in list(sys.stdin.readline().split()):
                hour, min, sec = t[1] if t[0] == "0" else t[:2], t[4] if t[3] == "0" else t[3:5], t[7] if t[6] == "0" else t[6:]
                if not s:
                    times[convert(int(hour), int(min), int(sec))] += 1
                    s = True
                else:
                    times[convert(int(hour), int(min), int(sec))] -= 1
        for i in range(1, 24 * 3600 + 1):
            times[i] += times[i - 1]
        print(max(times))
        


if __name__ == '__main__':
    main()
