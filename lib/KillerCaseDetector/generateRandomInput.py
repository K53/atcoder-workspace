import warnings
import sys
import random
import bisect
import string
import time
import re
from collections import deque
from collections import defaultdict

FORMAT_CONFIG = "config_format.txt"
CONDITION_CONFIG = "config_condition.txt"
PARAMS = {}

class ReplacableParameter():
    def __init__(self, num_str: str, default_value: str = None) -> None:
        self.num_str = num_str
        self.default_value = default_value
    
    def getParameter(self, idx: int = 0): # Nなど
        try:
            if re.match('-?\d', self.num_str):
                return int(self.num_str)
            else:
                if self.num_str not in PARAMS and self.default_value is not None:
                    print("default_value was selected")
                    return int(self.default_value)
                if len(PARAMS[self.num_str]) == 1:
                    return PARAMS[self.num_str][0]
                else:
                    return PARAMS[self.num_str][idx]
        except Exception as e:
            print(f"[ERROR] Unknown length parameter : {self.num_str}, {idx} : {PARAMS}") # ここは例外発生してるのは正常 なんとかしたい
            raise e

class ElementCondition():
    def __init__(self, 
                 variable_name: str,
                 integer_min_val_replacable: ReplacableParameter = None,
                 integer_max_val_replacable: ReplacableParameter = None,
                 is_prime = False, 
                 string_candidates: int = None, 
                 string_length_replacable: ReplacableParameter = None,
                 eliminateDuplicatedElements: bool = False) -> None:
        
        """
            "variable_name": ${変数名},
            "integer_min_val_replacable": ${数値の最小値の文字列表記},
            "integer_max_val_replacable": ${数値の最小値の文字列表記},
            "is_prime": ${素数かどうか},
            "string_candidates": [${文字列の候補値},...],
            "string_length_replacable": ${文字列長の文字列表記},
            "eliminateDuplicatedElements": ${ True|False : 配列内の重複排除をするかどうか},
        """
        self.variable_name = variable_name
        self.integer_min_val_replacable = integer_min_val_replacable
        self.integer_max_val_replacable = integer_max_val_replacable
        self.is_prime = is_prime
        self.string_candidates = string_candidates
        self.string_length_replacable = string_length_replacable
        self.eliminateDuplicatedElements = eliminateDuplicatedElements
        self.type = None
        # self._validateRange()
    
    def setAttr(self, key: str, val: any):
        if key == "type":
            raise Exception("[ERROR] explicit change of 'type' parameter is not allowed.")
        if self.type is not None:
            raise Exception("[ERROR] parameter type has already fixed.")
        setattr(self, key, val)

    
    def _isIntegerCondition(self) -> bool:
        return self.integer_min_val_replacable is not None and \
        self.integer_max_val_replacable is not None and \
        self.is_prime == False and \
        self.string_candidates is None and \
        self.string_length_replacable is None
    
    def _isPrimeIntegerCondition(self) -> bool:
        return self.integer_min_val_replacable is not None and \
        self.integer_max_val_replacable is not None and \
        self.is_prime == True and \
        self.string_candidates is None and \
        self.string_length_replacable is None
    
    def _isStringCondition(self) -> bool:
        return self.integer_min_val_replacable is None and \
        self.integer_max_val_replacable is None and \
        self.is_prime == False and \
        self.string_candidates is not None and \
        self.string_length_replacable is not None

    def getType(self):
        if self.type is not None:
            return self.type
        if self._isIntegerCondition():
            self.type = "int"
        elif self._isPrimeIntegerCondition():
            self.type = "prime"
        elif self._isStringCondition():
            self.type = "str"
        else:
            raise Exception("[ERROR] Condition parameter is invalid")
        return self.type

    def getIntegerMinVal(self, idx: int):
        return self.integer_min_val_replacable.getParameter(idx=idx)
    
    def getIntegerMaxVal(self, idx: int):
        return self.integer_max_val_replacable.getParameter(idx=idx)
    
    def getProvidableIntegerList(self, idx: int):
        return list(range(self.getIntegerMinVal(idx=idx), self.getIntegerMaxVal(idx=idx) + 1))

    def getStringLength(self, idx: int):
        return self.string_length_replacable.getParameter(idx=idx)
    
class ListCondition():
    def __init__(self, length_replacable: ReplacableParameter = ReplacableParameter(num_str="1"), allowDuplicatedElementsInList = True) -> None:
        self.length_replacable = length_replacable
        self.allowDuplicatedElementsInList = allowDuplicatedElementsInList   
    
    def getLength(self):
        return self.length_replacable.getParameter()
    
class PairCondition():
    def __init__(self, 
                 allowDuplicatedElementsInPair = True,
                 allowUnsortedElementsInPair = True,
                 allowDuplicatedPairInLists = True) -> None:
        self.allowDuplicatedElementsInPair = allowDuplicatedElementsInPair
        self.allowUnsortedElementsInPair = allowUnsortedElementsInPair
        self.allowDuplicatedPairInLists = allowDuplicatedPairInLists
    
class RandIntListGenerator():
    def __init__(self, variable_names: "list[str]", tmp_username: str) -> None:
        self.variable_names = variable_names
        self.element_conditions: "list[ElementCondition]" = []
        self.list_conditions: "list[ListCondition]" = []
        self.pair_conditions: "list[PairCondition]" = []
        self.tmp_username = tmp_username

    def generateParameter(self) -> "dict[str, dict[str, int|list]]":
        """
        {
            "A B": {
                "A": [1],
                "B": [3],
            },
            "C" : {
                "C": [1, 2, 3]
            }
        }
        """
        # print(self.variable_names)
        # print(self.element_conditions)
        # print(self.list_conditions)
        # print(self.pair_conditions)
        if len(self.pair_conditions) == 0:
            if self.list_conditions[0].allowDuplicatedElementsInList:
                if self.element_conditions[0].getType() == "str":
                    return {
                        self.variable_names: {
                            self.variable_names: ["".join(random.choices(self.element_conditions[0].string_candidates, k=self.element_conditions[0].getStringLength(idx=idx))) for idx in range(self.list_conditions[0].getLength())]
                        }
                    }
                elif self.element_conditions[0].getType() == "prime":
                    res = []
                    sys.path.append(f"/Users/{self.tmp_username}/atcoder-workspace/lib/")
                    from Eratosthenes import Eratosthenes
                    eratosthenes = Eratosthenes(1000)
                    all_primes = eratosthenes.primes
                    for idx in range(self.list_conditions[0].getLength()):
                        min_idx = bisect.bisect_left(all_primes, self.element_conditions[0].getIntegerMinVal(idx=idx))
                        max_idx = bisect.bisect_left(all_primes, self.element_conditions[0].getIntegerMaxVal(idx=idx))
                        primes = all_primes[min_idx:(max_idx + 1)]
                        res.append(random.choices(primes, k=1))
                    return {
                        self.variable_names: {
                            self.variable_names: res
                        }
                    }
                else:
                    return {
                        self.variable_names: {
                            self.variable_names: [random.randint(self.element_conditions[0].getIntegerMinVal(idx=idx), self.element_conditions[0].getIntegerMaxVal(idx=idx)) for idx in range(self.list_conditions[0].getLength())]
                        }
                    }
            else:
                if self.element_conditions[0].getType() == "str":
                    warnings.warn("[WARN] We have not complemented this case. only idx=0")
                    return {
                        self.variable_names: {
                            self.variable_names: ["".join(random.choices(self.element_conditions[0].string_candidates, k=self.element_conditions[0].getStringLength(idx=idx))) for idx in range(self.list_conditions[0].getLength())]
                        }
                    }
                else:
                    warnings.warn("[WARN] We have not complemented this case. only idx=0")
                    l = self.element_conditions[0].getProvidableIntegerList(idx=0)
                    if len(l) < self.list_conditions[0].getLength():
                        raise Exception(f"[ERROR] value range must be longer than directed length with eliminateDuplicatedElements option.: {len(l)} {self.list_conditions[0].getLength()}")
                    random.shuffle(l)
                    return {
                        self.variable_names: {
                            self.variable_names: l[:self.list_conditions[0].getLength()]
                        }
                    }
        elif len(self.pair_conditions) == 1:
            warnings.warn("[WARN] We have not complemented this case. ループしてマージすると重複するケースあり")
            if len(set([condition.getLength() for condition in self.list_conditions])) > 1:
                raise Exception("[ERROR] All lists in a pair must be same length.")
            pairs = set()
            rest_length = self.list_conditions[0].getLength()
            res_lists = defaultdict(list)
            start_loop = time.time()
            while rest_length > 0:
                if time.time() - start_loop > 2:
                    raise Exception("[ERROR] Eligible Pair was not found.")
                tmp_lists = {}
                for condition in self.element_conditions:
                    key = condition.variable_name
                    if condition.getType() == "int":
                        min_val, max_val = condition.getIntegerMinVal(idx=0), condition.getIntegerMaxVal(idx=0) # 暫定0indexのみ
                        tmp_lists[key] = genRandIntList(
                            min_val=min_val, 
                            max_val=max_val, 
                            length=rest_length, 
                            eliminateDuplicatedElements=not self.list_conditions[0].allowDuplicatedElementsInList)
                    # else: # condition.getType() == "st"
                    #     string_min_length, string_max_length, string_candidates = condition.string_min_length, condition.string_max_length, condition.string_candidates
                    #     tmp_lists[key] = genRandStrList(string_min_length, string_max_length, string_candidates, rest_length)

                for i in range(rest_length):
                    pair = tuple(l[i] for l in tmp_lists.values())
                    
                    # variable^1 ≦ ... ≦ variable^N でない場合を排除
                    if not self.pair_conditions[0].allowUnsortedElementsInPair:
                        if pair != tuple(sorted(pair)):
                            continue
                    
                    # 全ての要素が同じである場合を排除
                    if not self.pair_conditions[0].allowDuplicatedElementsInPair:
                        if len(set([num for num in pair])) == 1:
                            continue
                    
                    # (variable^1, ..., variable^N)のペアの重複を排除
                    if not self.pair_conditions[0].allowDuplicatedPairInLists:
                        if pair in pairs:
                            continue
                        pairs.add(pair)
                    
                    for key, l in tmp_lists.items():
                        res_lists[key].append(l[i])
                    rest_length -= 1

            return {
                self.variable_names: res_lists
            }
        else:
            raise Exception("[ERROR] ###")

class ParameterWriter():
    def __init__(self, variable_names: "list[str]", vertical = False) -> None:
        self.variable_names = variable_names
        self.vertical = vertical
    
    def write(self, file_handler) -> None:
        output_list = [PARAMS[variable_name] for variable_name in self.variable_names]
        output_line_strings = []
        if self.vertical:
            if len(set([len(L) for L in output_list])) != 1:
                raise Exception("[ERROR] lists must be same length.")
            for variables_on_same_line in zip(*output_list):
                output_line_strings.append(" ".join(list(map(str, variables_on_same_line))))
            delimiter = "\n"
        else:
            for variables_on_same_line in output_list:
                output_line_strings.append(" ".join(list(map(str, variables_on_same_line))))
            delimiter = " "
        file_handler.write(delimiter.join(output_line_strings))
        file_handler.write("\n")

class ConditionManager:
    def __init__(self) -> None:
        self.element_conditions: "dict[str, ElementCondition]" = {}
        self.list_conditions: "dict[str, ListCondition]" = {}
        self.pair_conditions: "dict[str, PairCondition]" = {}

    def addElementCondition(self, variable_name: str, conditions: "dict[str, int|str|list|ReplacableParameter]" = {}):
        if variable_name not in self.element_conditions:
            self.element_conditions[variable_name] = ElementCondition(**conditions)
        else:
            for condition_key, condition_value in conditions.items():
                self.element_conditions[variable_name].setAttr(condition_key, condition_value)
    
    def addListCondition(self, variable_name: str, conditions: "dict[str, int|str|list|ReplacableParameter]" = {}):
        if variable_name not in self.list_conditions:
            self.list_conditions[variable_name] = ListCondition(**conditions)
            for condition_key, condition_value in conditions.items():
                print(getattr(self.list_conditions[variable_name], condition_key))
        else:
            for condition_key, condition_value in conditions.items():
                setattr(self.list_conditions[variable_name], condition_key, condition_value)
    
    def registerPairCondition(self, variable_name: str, condition: PairCondition):
        if type(condition) == PairCondition:
            self.pair_conditions[variable_name] = condition


def genRandIntList(min_val: int, max_val: int, length: int = 1, eliminateDuplicatedElements: bool = False) -> "list[int]":
    if min_val > max_val:
        raise Exception(f"min_val ({min_val}) > max_val ({max_val})")
    
    if eliminateDuplicatedElements:
        if max_val - min_val + 1 < length:
            raise Exception("[ERROR] value range must be longer than dorected length with eliminateDuplicatedElements option.")
        l = list(range(min_val, max_val + 1))
        random.shuffle(l)
        return l[:length]
    else:
        return [random.randint(min_val, max_val) for _ in range(length)]

conditionMgr = ConditionManager()
generators = {}

writers = []
def readFormat(line):
    if "(" in line and "[" in line:
        idx_pair_l, idx_pair_r = line.index("("), line.index(")")
        variable_name_with_space = line[(idx_pair_l + 1):(idx_pair_r - 1 + 1)] # "C D"
        variable_names = variable_name_with_space.split(" ")    # ["C", "D"]
        idx_bracket_l, idx_bracket_r = line.index("["), line.index("]")
        isVertical = True if line[idx_bracket_l + 1] == ":" else False
        writers.append(ParameterWriter(variable_names=variable_names, vertical=isVertical))
    elif "[" in line:
        idx_bracket_l, idx_bracket_r = line.index("["), line.index("]")
        variable_name = line[idx_bracket_l - 1]
        variable_names = [variable_name]
        isVertical = True if line[idx_bracket_l + 1] == ":" else False
        writers.append(ParameterWriter(variable_names=variable_names, vertical=isVertical))
    else:
        variable_name_with_space = line # "N M"
        variable_names = variable_name_with_space.split(" ") # ["N", "M"]
        writers.append(ParameterWriter(variable_names=variable_names))

generator_kinds = list()
def readCondition(line: str):
    line_splitted = line.split(" ")
    pairs = []
    if line_splitted[0] == "+":
        if line_splitted[2] == "/=":
            if line_splitted[1] == line_splitted[3]: # 同一配列内の要素間での制約
                variable_name = line_splitted[1]
                conditionMgr.list_conditions[variable_name].allowDuplicatedElementsInList = False
            else:
                conbined = " ".join([line_splitted[1], line_splitted[3]])
                conditionMgr.registerPairCondition(
                    variable_name=conbined, 
                    condition=PairCondition(
                        allowDuplicatedElementsInPair=False,
                    )
                )
                pairs.append([line_splitted[1], line_splitted[3]])
                generator_kinds.remove(line_splitted[1])
                generator_kinds.remove(line_splitted[3])
                generator_kinds.append(conbined)

    else:
        if "{" in line_splitted[3]:
            candidates = []
            paramter_type = "str"
            for component in line_splitted[3][1:-1].split(","):
                if component == "a":
                    candidates.extend([ch for ch in string.ascii_lowercase])
                elif component == "A":
                    candidates.extend([ch for ch in string.ascii_uppercase])
                elif component == "0":
                    candidates.extend([str(i) for i in range(0, 10)])
                elif component == "prime":
                    paramter_type = "prime"
                elif '"' in component or "'" in component:
                    candidates.append(component[1:-1])
                else:
                    raise Exception("[ERROR] Unknown candidate")
            
            variable_name = line_splitted[0]
            if paramter_type == "str":
                conditionMgr.addElementCondition(
                    variable_name=variable_name, 
                    conditions={
                        "variable_name": variable_name,
                        "string_candidates": candidates,
                        "string_length_replacable": ReplacableParameter(num_str=f"|{variable_name}|", default_value="1")    # |S|が提供されない場合はselectの挙動とするためdefault_value=1
                    }
                )
            elif paramter_type == "prime":
                conditionMgr.addElementCondition(
                    variable_name=variable_name, 
                    conditions={
                        "variable_name": variable_name,
                        "is_prime": True,
                    }
                )
            else:
                raise Exception("[ERROR]")

        else:
            variable_name = line_splitted[0]
            conditionMgr.addElementCondition(
                variable_name=variable_name, 
                conditions={
                    "variable_name": variable_name,
                    "integer_min_val_replacable": ReplacableParameter(num_str=line_splitted[1]),
                    "integer_max_val_replacable": ReplacableParameter(num_str=line_splitted[5])
                }
            )
        generator_kinds.append(variable_name)
        if "[" in line_splitted[3]:# and "|" in line_splitted[3]:
            idx_bracket_l, idx_bracket_r = line_splitted[3].index("["), line_splitted[3].index("]")
            conditionMgr.addListCondition(
                variable_name=variable_name, 
                conditions={
                    "length_replacable": ReplacableParameter(num_str=line_splitted[3][(idx_bracket_l + 1):idx_bracket_r])
                }
            )
        elif "[" in line_splitted[1]:
            print(line)
            idx_bracket_l, idx_bracket_r = line_splitted[1].index("["), line_splitted[1].index("]")
            conditionMgr.addListCondition(
                variable_name=variable_name, 
                conditions={
                    "length_replacable": ReplacableParameter(num_str=line_splitted[1][(idx_bracket_l + 1):idx_bracket_r])
                }
            )
        else:
            conditionMgr.addListCondition(
                variable_name=variable_name
            )

    return pairs

def main():
    args = sys.argv
    _, condition_config_file_name, format_config_file_name, out_file_name, tmp_username = args[0], args[1], args[2], args[3], args[4]
    CONDITION_CONFIG = condition_config_file_name
    FORMAT_CONFIG = format_config_file_name
    
    # 条件ファイルの読み込み
    with open(CONDITION_CONFIG, "r") as condition_config:
        for line in [line.rstrip() for line in condition_config.readlines()]:
            if line == "":
                break
            readCondition(line=line)

    for g in generator_kinds:
        generators[g] = RandIntListGenerator(variable_names=g, tmp_username=tmp_username)
        if g in conditionMgr.pair_conditions.keys():
            generators[g].pair_conditions = [conditionMgr.pair_conditions[g]]
        generators[g].element_conditions = [conditionMgr.element_conditions[variable_name] for variable_name in g.split(" ")]
        generators[g].list_conditions = [conditionMgr.list_conditions[variable_name] for variable_name in g.split(" ") if variable_name in conditionMgr.list_conditions]
    
    # 書式ファイルの読み込み
    with open(FORMAT_CONFIG, "r") as format_config:
        for line in [line.rstrip() for line in format_config.readlines()]:
            if line == "":
                break
            readFormat(line=line)

    q = deque(generators.values())
    q.append(None)
    stop = False
    while len(q) > 0:
        g = q.popleft()
        if g is None:
            stop = True
            continue
        try:
            generated_parameters = g.generateParameter()
        except Exception as e:
            if stop:
                raise e
            else:
                q.append(g)
                continue
        for variable_names, generated in generated_parameters.items():
            for variable_name in variable_names.split(" "):
                PARAMS[variable_name] = generated[variable_name]
    
    print(PARAMS, "''")
    with open(out_file_name, "w") as handler:
        for w in writers:
            w.write(handler)
    return
    

if __name__ == '__main__':
    main()




    
    
    # https://atcoder.jp/contests/abc337/tasks/abc337_c
    # https://atcoder.jp/contests/abc337/tasks/abc337_g 木
    # https://atcoder.jp/contests/abc201/tasks/abc201_e 重み付き木
    # https://atcoder.jp/contests/abc202/tasks/abc202_e 木 input形式keisiki異なる
    # https://atcoder.jp/contests/abc344/tasks/abc344_e クエリ そのクエリがくるときには既に要素が存在することが保証
    # https://atcoder.jp/contests/abc212/tasks/abc212_d クエリ そのクエリがくるときには既に要素が存在することが保証
    # https://atcoder.jp/contests/abc202/tasks/abc202_f 図形 同一直線上にない



    # C = genRandElementListsWithConditions(
    #     ElementConditions={
    #         "C": {
    #             "candidates": ["R", "L", "U", "D"],
    #         },
    #     },
    #     length=N,
    # )
    # print(C["C"])