#!/usr/bin/env python3
from collections import deque
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, default_value: int = -1) -> None:
        self.val = default_value
        self.prev = None
    
    def add(self, next: "Node"):
        next.prev = self
        return next
    
    def delete(self):
        return self if self.val == -1 else self.prev

def main():
    currents = []
    

if __name__ == '__main__':
    main()
