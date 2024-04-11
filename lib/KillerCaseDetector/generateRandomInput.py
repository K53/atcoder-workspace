import warnings
import sys
import random
import bisect
import string
import time
import re
from collections import deque, defaultdict

CONDITION_LOWERCASES = "a"
CONDITION_UPPERCASES = "A"
CONDITION_NUMBERS = "0"
CONDITION_PRIMES = "prime"

GENERATOR_TYPE_LIST = "list"
GENERATOR_TYPE_GRID = "grid"
GENERATOR_TYPE_PAIR = "pair"

ELEMENT_CONDITION_TYPE_STRING = "str"
ELEMENT_CONDITION_TYPE_PRIME = "prime"

class FixedParams():
    def __init__(self) -> None:
        self.parameters = {}
    
    def setParams(self, variable_name: str, value: "list[int|str|list]") -> None:
        self.parameters[variable_name] = value
    
    def __str__(self) -> str:
        return "\n".join([f"{k}: {val}" for k, val in self.parameters.items()])

class ReplacableParameter():
    def __init__(self, num_str: str, default_value: str = None) -> None:
        self.num_str = num_str
        self.default_value = default_value
        self.skip_count = 0
        self.calced = None
    
    def _calc(self):
        if self.calced is not None:
            return self.calced
        if self.num_str[0] == "(" and self.num_str[-1] == ")":
            formula = self.num_str[1:-1]
            if "*" in formula:
                self.calced = 1
                for param in formula.split("*"):
                    self.calced *= ReplacableParameter(num_str=param).getParameter()
            if "/" in formula:
                if self.calced is not None:
                    raise Exception("[NOT IMPREMENTED] Now, ReplacableParameter calcuration support to process only one operator")
                params = formula.split("/")
                if len(params) > 2:
                    raise Exception("[NOT IMPREMENTED] Now, ReplacableParameter calcuration support to divide with only one operator")
                self.calced = ReplacableParameter(num_str=params[0]).getParameter() // ReplacableParameter(num_str=params[1]).getParameter()
            if "+" in formula:
                if self.calced is not None:
                    raise Exception("[NOT IMPREMENTED] Now, ReplacableParameter calcuration support to process only one operator")
                self.calced = 0
                for param in formula.split("+"):
                    self.calced += ReplacableParameter(num_str=param).getParameter()
            if "-" in formula:
                if self.calced is not None:
                    raise Exception("[NOT IMPREMENTED] Now, ReplacableParameter calcuration support to process only one operator")
                params = formula.split("-")
                if len(params) > 2:
                    raise Exception("[NOT IMPREMENTED] Now, ReplacableParameter calcuration support to subtract with only one operator")
                self.calced = ReplacableParameter(num_str=params[0]).getParameter() - ReplacableParameter(num_str=params[1]).getParameter()
            return self.calced
        else:
            return None

    def getParameter(self, idx: int = 0):
        calced = self._calc()
        if calced is not None:
            return calced
        
        if re.match('-?\d', self.num_str):
            return int(self.num_str)
        else:
            if self.num_str in fixed_params.parameters:
                if len(fixed_params.parameters[self.num_str]) == 1:
                    return fixed_params.parameters[self.num_str][0]
                else:
                    return fixed_params.parameters[self.num_str][idx]
            else:
                if self.skip_count > 0 and self.default_value is not None:
                    print("default_value was selected")
                    return int(self.default_value)     
                else:
                    self.skip_count += 1
                    print(f"[ERROR] Unknown length parameter : {self.num_str}, {idx} : {fixed_params}") # ここは例外発生してるのは正常 なんとかしたい
                    raise ValueError("[ERROR] parameter is not defined.")       ## default_valueは廃止予定 |L|がなければdefault_valueで同時に作成する方が望ましい。
        # except Exception as e:
        #     print(f"[ERROR] Unknown length parameter : {self.num_str}, {idx} : {fixed_params}") # ここは例外発生してるのは正常 なんとかしたい
        #     raise e
    
    def __str__(self) -> str:
        return f"{self.num_str}: {self.getParameter()}, default_value: {self.default_value}"

class ElementCondition():
    def __init__(self):
        self.variable_name: str = None
        self.integer_min_val_replacable: ReplacableParameter = None
        self.integer_max_val_replacable: ReplacableParameter = None
        self.is_prime = False
        self.string_candidates: int = None
        self.string_length_replacable: ReplacableParameter = None
        self.eliminateDuplicatedElements = False
        self.type: str = None
    
    def setAttr(self, key: str, val: any):
        if key == "type":
            raise Exception("[ERROR] explicit change of 'type' parameter is not allowed.")
        if self.type is not None:
            raise Exception("[ERROR] parameter type has already fixed.")
        if self.integer_min_val_replacable is not None and self.integer_max_val_replacable is not None and self.integer_min_val_replacable.getParameter(idx=0) > self.integer_max_val_replacable.getParameter(idx=0):
            raise Exception("[ERROR] integer_min_val imust be less than integer_max")
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
            self.type = ELEMENT_CONDITION_TYPE_PRIME
        elif self._isStringCondition():
            self.type = ELEMENT_CONDITION_TYPE_STRING
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
    
    def __str__(self) -> str:
        return f"{self.string_length_replacable}"

class ListCondition():
    def __init__(self, length_replacable: ReplacableParameter = ReplacableParameter(num_str="1"), allowDuplicatedElementsInList = True) -> None:
        self.length_replacable = length_replacable
        self.allowDuplicatedElementsInList = allowDuplicatedElementsInList   
    
    def getLength(self):
        return self.length_replacable.getParameter()

class GridCondition():
    def __init__(self, width_length_replacable: ReplacableParameter, height_length_replacable: ReplacableParameter, allowDuplicatedElementsInList = True) -> None:
        self.width_length_replacable = width_length_replacable
        self.height_length_replacable = height_length_replacable
        self.allowDuplicatedElementsInList = allowDuplicatedElementsInList
    
    def getWidth(self):
        return self.width_length_replacable.getParameter()
    
    def getHeight(self):
        return self.height_length_replacable.getParameter()

    def __str__(self) -> str:
        return f"{self.width_length_replacable}, {self.height_length_replacable}"
    
class PairCondition():
    def __init__(self, 
                 allowDuplicatedElementsInPair = True,
                 allowUnsortedElementsInPair = True,
                 allowDuplicatedPairInLists = True) -> None:
        self.allowDuplicatedElementsInPair = allowDuplicatedElementsInPair
        self.allowUnsortedElementsInPair = allowUnsortedElementsInPair
        self.allowDuplicatedPairInLists = allowDuplicatedPairInLists
    
class RandIntListGenerator():
    eratosthenes = None
    def __init__(self, variable_names: "list[str]", tmp_username: str) -> None:
        self.variable_names = variable_names
        self.element_conditions: "list[ElementCondition]" = []
        self.list_conditions: "list[ListCondition]" = []
        self.grid_conditions: "list[GridCondition]" = []
        self.pair_conditions: "list[PairCondition]" = []
        self.tmp_username = tmp_username

    def _getGeneratorType(self):
        if len(self.pair_conditions) > 1:
            raise Exception("[ERROR] Not Defined and Implemented")
        if len(self.grid_conditions) > 1:
            raise Exception("[ERROR] Not Defined and Implemented")
        if len(self.pair_conditions) > 0 and len(self.grid_conditions) == 0:
            return GENERATOR_TYPE_PAIR
        if len(self.pair_conditions) == 0 and \
            len(self.grid_conditions) == 1 and \
            len(self.list_conditions) == 0 and \
            len(self.element_conditions) == 1:
            return GENERATOR_TYPE_GRID
        if len(self.pair_conditions) == 0 and \
            len(self.grid_conditions) == 0 and \
            len(self.list_conditions) == 1 and \
            len(self.element_conditions) == 1:
            return GENERATOR_TYPE_LIST
        raise Exception("[NOT IMPREMENTED] Unexpected Case")

    @classmethod
    def initEratosthenes(cls):
        from Eratosthenes import Eratosthenes
        cls.eratosthenes = Eratosthenes(10000)

    def _generateStrList(self, duplicatable=True):
        res = []
        candidates = self.element_conditions[0].string_candidates
        for idx in range(self.list_conditions[0].getLength()):
            element_count = self.element_conditions[0].getStringLength(idx=idx)
            print(self.element_conditions[0])
            if duplicatable:
                res.append("".join(random.choices(candidates, k=element_count)))
            else:
                if len(candidates) < element_count:
                    raise Exception(f"[ERROR] candidates length ({len(candidates)} : {candidates}) must be larger than element_count ({element_count}).")
                res.append("".join(random.sample(candidates, k=element_count)))
        
        return { self.variable_names: { self.variable_names: res } }
                         
    def _generateIntegerList(self, prime=False, duplicatable=True):
        ### 移設予定
        sys.path.append(f"/Users/{self.tmp_username}/atcoder-workspace/lib/")   # 場所ー＞ class変数に持ってく
        RandIntListGenerator.initEratosthenes()
        
        res = []
        for idx in range(self.list_conditions[0].getLength()):
            if duplicatable:
                if prime:
                    all_primes = RandIntListGenerator.eratosthenes.primes
                    min_idx = bisect.bisect_left(all_primes, self.element_conditions[0].getIntegerMinVal(idx=idx))
                    max_idx = bisect.bisect_left(all_primes, self.element_conditions[0].getIntegerMaxVal(idx=idx))
                    primes = all_primes[min_idx:max_idx]        # candidates生成はConditionクラウ移植？
                    res.append(random.choice(primes))
                else:
                    min_val = self.element_conditions[0].getIntegerMinVal(idx=idx)
                    max_val = self.element_conditions[0].getIntegerMaxVal(idx=idx)
                    res.append(random.randint(min_val, max_val))
            else:
                if prime:
                    raise Exception("[ERROR] NOT IMPREMENTED")
                else:
                    candidates = self.element_conditions[0].getProvidableIntegerList(idx=0)
                    element_count = self.list_conditions[0].getLength()
                    if len(candidates) < element_count:
                        raise Exception(f"[ERROR] candidates length ({len(candidates)} : {candidates}) must be larger than element_count ({element_count}).")
                    random.shuffle(candidates)
                    return {
                        self.variable_names: {
                            self.variable_names: candidates[:element_count]
                        }
                    }

        return { self.variable_names: { self.variable_names: res } }

    def _generateStringGrid(self, duplicatable=True):
        raise Exception("[NOT IMPREMENTED]")

    def _generateIntegerGrid(self, prime=False, duplicatable=True):
        res = []
        if duplicatable:
            if prime:
                raise Exception("[NOT IMPREMENTED]")
            else:
                for _ in range(self.grid_conditions[0].getHeight()):
                    line = []
                    for idx in range(self.grid_conditions[0].getWidth()):
                        min_val = self.element_conditions[0].getIntegerMinVal(idx=idx)
                        max_val = self.element_conditions[0].getIntegerMaxVal(idx=idx)
                        line.append(random.randint(min_val, max_val))
                    res.append(line)
        else:
            if prime:
                raise Exception("[NOT IMPREMENTED]")
            else:
                raise Exception("[NOT IMPREMENTED]")
        return { self.variable_names: { self.variable_names: res } }

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
        if self._getGeneratorType() == GENERATOR_TYPE_LIST:
            if self.list_conditions[0].allowDuplicatedElementsInList:       # LISTとGRIDは統合したい
                if self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_STRING:
                    return self._generateStrList()
                elif self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_PRIME:
                    return self._generateIntegerList(prime=True)
                else:
                    return self._generateIntegerList()
            else:
                if self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_STRING:
                    return self._generateStrList(duplicatable=False)
                elif self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_PRIME:
                    return self._generateIntegerList(prime=True, duplicatable=False)
                else:
                    return self._generateIntegerList(duplicatable=False)

        elif self._getGeneratorType() == GENERATOR_TYPE_GRID:
            if self.grid_conditions[0].allowDuplicatedElementsInList:
                if self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_STRING:
                    return self._generateStringGrid()
                elif self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_PRIME:
                    return self._generateIntegerGrid(prime=True)
                else:
                    return self._generateIntegerGrid()
            else:
                if self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_STRING:
                    return self._generateStringGrid(duplicatable=False)
                elif self.element_conditions[0].getType() == ELEMENT_CONDITION_TYPE_PRIME:
                    return self._generateIntegerGrid(prime=True, duplicatable=False)
                else:
                    return self._generateIntegerGrid(duplicatable=False)
        
        elif self._getGeneratorType() == GENERATOR_TYPE_PAIR:
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
                        if self.list_conditions[0].allowDuplicatedElementsInList:
                            tmp_lists[key] = [random.randint(condition.getIntegerMinVal(idx=0), condition.getIntegerMaxVal(idx=0)) for _ in range(rest_length)] # 暫定0indexのみ
                        else:
                            l = condition.getProvidableIntegerList(idx=0)
                            if len(l) < rest_length:
                                raise Exception(f"[ERROR] value range must be longer than directed length with eliminateDuplicatedElements option.: {len(l)} {self.list_conditions[0].getLength()}")
                            random.shuffle(l)
                            tmp_lists[key] = l[:rest_length]


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
            raise Exception("[ERROR Unexpected case")

class ParameterWriter():
    def __init__(self, variable_names: "list[str]", vertical = False, grid = False) -> None:
        self.variable_names = variable_names
        self.vertical = vertical
        self.grid = grid
    
    def write(self, file_handler) -> None:
        output_line_strings = []
        if self.grid:
            for variables_on_same_line in fixed_params.parameters[self.variable_names[0]]:
                output_line_strings.append(" ".join(list(map(str, variables_on_same_line))))
            delimiter = "\n"
        else:
            output_list = [fixed_params.parameters[variable_name] for variable_name in self.variable_names]
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
        self.element_conditions: "dict[str, ElementCondition]" = defaultdict(ElementCondition)
        self.list_conditions: "dict[str, ListCondition]" = {}
        self.grid_conditions: "dict[str, GridCondition]" = {}
        self.pair_conditions: "dict[str, PairCondition]" = {}

    def addElementCondition(self, variable_name: str, conditions: "dict[str, int|str|list|ReplacableParameter]" = {}, overwritable = True):
        for condition_key, condition_value in conditions.items():
            if not overwritable and getattr(self.element_conditions[variable_name], condition_key) is None:
                # raise("[ERROR] Overwrite")
                return
            self.element_conditions[variable_name].setAttr(condition_key, condition_value)
    
    def addListCondition(self, variable_name: str, conditions: "dict[str, int|str|list|ReplacableParameter]" = {}):
        if variable_name not in self.list_conditions:
            self.list_conditions[variable_name] = ListCondition(**conditions)
        else:
            for condition_key, condition_value in conditions.items():
                setattr(self.list_conditions[variable_name], condition_key, condition_value)
    
    def addGridCondition(self, variable_name: str, conditions: "dict[str, int|str|list|ReplacableParameter]" = {}):
        if variable_name not in self.grid_conditions:
            self.grid_conditions[variable_name] = GridCondition(**conditions)
        else:
            for condition_key, condition_value in conditions.items():
                setattr(self.grid_conditions[variable_name], condition_key, condition_value)
    
    def registerPairCondition(self, variable_name: str, condition: PairCondition):
        if type(condition) == PairCondition:
            self.pair_conditions[variable_name] = condition
    
def getIndicies(L: "str|list", target: "str|int"):
    return [idx for idx, val in enumerate(L) if val == target]

condition_mgr = ConditionManager()
fixed_params = FixedParams()
generators: "dict[str, RandIntListGenerator]" = {}

writers = []
def readFormat(line: str):
    if "(" in line and "[" in line:
        idx_pair_l, idx_pair_r = line.index("("), line.index(")")
        variable_name_with_space = line[(idx_pair_l + 1):(idx_pair_r - 1 + 1)] # "C D"
        variable_names = variable_name_with_space.split(" ")    # ["C", "D"]
        idx_bracket_l, idx_bracket_r = line.index("["), line.index("]")
        isVertical = True if line[idx_bracket_l + 1] == ":" else False
        writers.append(ParameterWriter(variable_names=variable_names, vertical=isVertical))
    elif line.count("[") == 2:
        idx_bracket_l, idx_bracket_r = line.index("["), line.index("]") # index()は最初に一致したインデックスを返すことを利用
        variable_name = line[idx_bracket_l - 1]
        variable_names = [variable_name]
        writers.append(ParameterWriter(variable_names=variable_names, grid=True))
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
                condition_mgr.list_conditions[variable_name].allowDuplicatedElementsInList = False
            else:
                conbined = " ".join([line_splitted[1], line_splitted[3]])
                condition_mgr.registerPairCondition(
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
            paramter_type = ELEMENT_CONDITION_TYPE_STRING
            for component in line_splitted[3][1:-1].split(","):
                if component == CONDITION_LOWERCASES:
                    candidates.extend([ch for ch in string.ascii_lowercase])
                elif component == CONDITION_UPPERCASES:
                    candidates.extend([ch for ch in string.ascii_uppercase])
                elif component == CONDITION_NUMBERS:
                    candidates.extend([str(i) for i in range(0, 10)])
                elif component == CONDITION_PRIMES:
                    paramter_type = ELEMENT_CONDITION_TYPE_PRIME
                elif '"' in component or "'" in component:
                    candidates.append(component[1:-1])
                else:
                    raise Exception("[ERROR] Unknown candidate")
            
            variable_name = line_splitted[0]
            if paramter_type == ELEMENT_CONDITION_TYPE_STRING:
                condition_mgr.addElementCondition(
                    variable_name=variable_name, 
                    conditions={
                        "variable_name": variable_name,
                        "string_candidates": candidates,
                        "string_length_replacable": ReplacableParameter(num_str=f"|{variable_name}|", default_value="1")    # |S|が提供されない場合はselectの挙動とするためdefault_value=1
                    }
                )
                # condition_mgr.addElementCondition(
                #     variable_name=variable_name, 
                #     conditions={
                #         "variable_name": f"|{variable_name}|",
                #         "integer_min_val_replacable": ReplacableParameter(1),
                #         "integer_max_val_replacable": ReplacableParameter(1)
                #     },
                #     overwritable=False
                # )
                # print([condition_mgr.element_conditions[i]. for  i in range(len(condition_mgr.element_conditions))])
            elif paramter_type == ELEMENT_CONDITION_TYPE_PRIME:
                condition_mgr.addElementCondition(
                    variable_name=variable_name, 
                    conditions={
                        "variable_name": variable_name,
                        "is_prime": True,
                    }
                )
            else:
                raise Exception("[NOT IMPLEMENTED]")

        else:
            variable_name = line_splitted[0]
            condition_mgr.addElementCondition(
                variable_name=variable_name, 
                conditions={
                    "variable_name": variable_name,
                    "integer_min_val_replacable": ReplacableParameter(num_str=line_splitted[1]),
                    "integer_max_val_replacable": ReplacableParameter(num_str=line_splitted[5])
                }
            )
        generator_kinds.append(variable_name)
        if line_splitted[3].count("[") == 2:
            indices_bracket_l = getIndicies(line_splitted[3], "[")
            indices_bracket_r = getIndicies(line_splitted[3], "]")
            condition_mgr.addGridCondition(
                variable_name=variable_name, 
                conditions={
                    "width_length_replacable": ReplacableParameter(num_str=line_splitted[3][(indices_bracket_l[0] + 1):indices_bracket_r[0]]),
                    "height_length_replacable": ReplacableParameter(num_str=line_splitted[3][(indices_bracket_l[1] + 1):indices_bracket_r[1]])
                }
            )
        elif "[" in line_splitted[3]:
            idx_bracket_l, idx_bracket_r = line_splitted[3].index("["), line_splitted[3].index("]")
            condition_mgr.addListCondition(
                variable_name=variable_name, 
                conditions={
                    "length_replacable": ReplacableParameter(num_str=line_splitted[3][(idx_bracket_l + 1):idx_bracket_r])
                }
            )
        elif "[" in line_splitted[1]:
            idx_bracket_l, idx_bracket_r = line_splitted[1].index("["), line_splitted[1].index("]")
            condition_mgr.addListCondition(
                variable_name=variable_name, 
                conditions={
                    "length_replacable": ReplacableParameter(num_str=line_splitted[1][(idx_bracket_l + 1):idx_bracket_r])
                }
            )
        else:
            condition_mgr.addListCondition(
                variable_name=variable_name
            )

    return pairs

def main():
    args = sys.argv
    _, condition_config_file_name, format_config_file_name, out_file_name, tmp_username = args[0], args[1], args[2], args[3], args[4]
    
    # 条件ファイルの読み込み
    with open(condition_config_file_name, "r") as condition_config:
        for line in [line.rstrip() for line in condition_config.readlines()]:
            if line == "":
                break
            readCondition(line=line)

    print(generator_kinds) # ペア条件の場合のみ"A B"みたいなのが入りうる。
    for g in generator_kinds:
        generators[g] = RandIntListGenerator(variable_names=g, tmp_username=tmp_username)
        if g in condition_mgr.pair_conditions.keys():
            generators[g].pair_conditions = [condition_mgr.pair_conditions[g]]
        generators[g].element_conditions = [condition_mgr.element_conditions[variable_name] for variable_name in g.split(" ")]
        generators[g].list_conditions = [condition_mgr.list_conditions[variable_name] for variable_name in g.split(" ") if variable_name in condition_mgr.list_conditions]
        generators[g].grid_conditions = [condition_mgr.grid_conditions[variable_name] for variable_name in g.split(" ") if variable_name in condition_mgr.grid_conditions]

    # 書式ファイルの読み込み
    with open(format_config_file_name, "r") as format_config:
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
                fixed_params.setParams(variable_name, generated[variable_name])
    
    print(fixed_params)
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