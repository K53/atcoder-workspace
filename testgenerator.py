from os import dup
import random
import string
from typing import List
import enum

class SortOrder(enum.Enum):
    NONE = enum.auto()
    ASCENDING = enum.auto()
    DESCENDING = enum.auto()

def getRandomSelect(arr: List, length: int, sortType: SortOrder = SortOrder.NONE, duplicatable: bool = False):
    if len(arr) < length:
        print("[NOTION] apply daplicate select mode.")
        duplicatable = True
    result = random.choices(arr, k=length) if duplicatable else random.sample(arr, length)
    if sortType == SortOrder.ASCENDING:
        result.sort()
    elif sortType == SortOrder.DESCENDING:
        result.sort(reverse=True)
    return result


def genRandomNumberArray(minimum: int, maximum: int, length: int, sortType: SortOrder = SortOrder.NONE, duplicatable: bool = False) -> List[int]:
    origin = [i for i in range(minimum, maximum + 1)]
    return getRandomSelect(origin, length, sortType, duplicatable)


def genRandomStringArray(startCharactor: str, endCharactor: str, length: int, sortType: SortOrder = SortOrder.NONE, duplicatable: bool = False) -> List[int]:
    isUpperCase = False
    if ord("a") <= ord(startCharactor) <= ord(endCharactor) <= ord("z"):
        isUpperCase = False
    elif ord("A") <= ord(startCharactor) <= ord(endCharactor) <= ord("Z"):
        isUpperCase = True
    else:
        raise("[Error] range error")
    origin = string.ascii_uppercase if isUpperCase else string.ascii_lowercase
    start = (ord(startCharactor) - ord("A")) if isUpperCase else (ord(startCharactor) - ord("a"))
    end = (ord(endCharactor) + 1 - ord("A")) if isUpperCase else (ord(endCharactor) + 1 - ord("a"))
    return getRandomSelect(origin[start:end], length, sortType, duplicatable)


# genRandomArray([4, 1, 0, 10, 7]) -> "4 1 0 10 7"
def toStringLine(line: List, separate: str = " ") -> str:
    origin = [str(l) for l in line]
    return separate.join(origin)

# genString("a", "c") -> "abc"
def genString(startCharactor: str, endCharactor: str, isUpperCase: bool = False) -> str:
    origin = string.ascii_uppercase if isUpperCase else string.ascii_lowercase
    start = (ord(startCharactor) - ord("A")) if isUpperCase else (ord(startCharactor) - ord("a"))
    end = (ord(endCharactor) + 1 - ord("A")) if isUpperCase else (ord(endCharactor) + 1 - ord("a"))
    return origin[start:end]



N = 300000
Q = 300000
K = 10

path = "./originaltest.txt"
with open(path, mode='w') as f:
    f.write(toStringLine([N]))
    f.write("\n")
    f.write(toStringLine(genRandomNumberArray(minimum=0, maximum=10 ** 9, length=N, sortType=SortOrder.NONE, duplicatable=True), separate=""))
    f.write("\n")
    # f.write(toStringLine([N]))
    # f.write("\n")
    # f.write(toStringLine(genRandomNumberArray(minimum=0, maximum=10 ** 9, length=Q, sortType=SortOrder.NONE, duplicatable=True), separate="\n"))
    # f.write("\n")






# "a" ~ "z"でK個のソートなし/重複なし
# f.write(toStringLine(genRandomStringArray(startCharactor="a", endCharactor="z", length=K, sortType=SortOrder.NONE, duplicatable=False), separate=""))