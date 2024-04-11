
# def genRandInt(rangeCondition: RangeCondition) -> int:
#     if rangeCondition.type != "int":
#         raise Exception("Invalid Parameter")
#     return random.randint(rangeCondition.getIntegerMinVal(), rangeCondition.getIntegerMaxVal())

# def genRandIntList(min_val: int, max_val: int, length: int = 1, eliminateDuplicatedElements: bool = False) -> "list[int]":
#     if min_val > max_val:
#         raise Exception(f"min_val ({min_val}) > max_val ({max_val})")
    
#     if eliminateDuplicatedElements:
#         if max_val - min_val + 1 < length:
#             raise Exception("[ERROR] value range must be longer than dorected length with eliminateDuplicatedElements option.")
#         l = list(range(min_val, max_val + 1))
#         random.shuffle(l)
#         return l[:length]
#     else:
#         return [random.randint(min_val, max_val) for _ in range(length)]

def genRandPrime(min_val: int, max_val: int, eratosthenes: Eratosthenes = None) -> None:
    if min_val > max_val:
        raise Exception(f"min_val ({min_val}) > max_val ({max_val})")
    if eratosthenes == None:
        eratosthenes = Eratosthenes(max_val)
    all_primes = eratosthenes.primes
    min_idx = bisect.bisect_left(all_primes, min_val)
    primes = all_primes[min_idx:]
    if len(primes) == 0:
        raise Exception("[ERROR] No primes belongs to directed range")
    return selectRandElementList(primes)[0]

# def genRandStr(rangeCondition: RangeCondition) -> str:
#     if rangeCondition.type != "str":
#         raise Exception("Invalid Parameter")
#     return "".join(selectRandElementList(rangeCondition.string_candidates, random.randint(rangeCondition.string_min_length, rangeCondition.string_max_length)))

# def genRandStrList(min_length: int, 
#                    max_length: int, 
#                    candidates: list = string.ascii_lowercase, 
#                    list_length: int = 1, 
#                    eliminateDuplicatedElements: bool = False) -> "list[str]":
#     if eliminateDuplicatedElements:
#         raise("[ERROR] this option is not implemented yet.")
#     return [genRandStr(min_length, max_length, candidates) for _ in range(list_length)]

# def selectRandElement(source_list: list) -> "int|str":
#     return selectRandElementList(source_list)[0]

# def selectRandElementList(source_list: list, length: int = 1, eliminateDuplicatedElements: bool = False) -> "list[int|str]":
#     if eliminateDuplicatedElements:
#         if len(source_list) < length:
#             raise Exception("[ERROR] source_list must be longer than dorected length with eliminateDuplicatedElements option.")
#         random.shuffle(source_list)
#         return source_list[:length]
#     else:
#         if len(source_list) == 0:
#             raise Exception("[ERROR] source_list nust be longer than 0.")
#         return random.choices(source_list, k=length)

# def genRandValPairsWithConditions(
#         pairCondition: PairCondition
#     ) -> dict:
#     pairs = set()
#     rest_length = pairCondition.length
#     res_lists = defaultdict(list)
#     start_loop = time.time()
#     while rest_length > 0:
#         if time.time() - start_loop > 2:
#             raise Exception("[ERROR] Eligible Pair was not found.")
#         tmp_lists = {}
#         for condition in pairCondition.rangeConditions:
#             key = condition.variable_name
#             if condition.type == "int":
#                 min_val, max_val = condition.integer_min_val, condition.integer_max_val
#                 tmp_lists[key] = genRandIntList(
#                     min_val=min_val, 
#                     max_val=max_val, 
#                     length=rest_length, 
#                     eliminateDuplicatedElements=condition.eliminateDuplicatedElements)
#             elif condition.type == "select":
#                 candidates = condition.select_candidates
#                 tmp_lists[key] = selectRandElementList(candidates, rest_length)
#             else: # condition.type == "st"
#                 string_min_length, string_max_length, string_candidates = condition.string_min_length, condition.string_max_length, condition.string_candidates
#                 tmp_lists[key] = genRandStrList(string_min_length, string_max_length, string_candidates, rest_length)

#         for i in range(rest_length):
#             pair = tuple(l[i] for l in tmp_lists.values())
            
#             # variable^1 ≦ ... ≦ variable^N でない場合を排除
#             if pairCondition.eliminateUnsortedPair:
#                 if pair != tuple(sorted(pair)):
#                     continue
            
#             # 全ての要素が同じである場合を排除
#             if pairCondition.eliminateAllSameElementsPair:
#                 if len(set([num for num in pair])) == 1:
#                     continue
            
#             # (variable^1, ..., variable^N)のペアの重複を排除
#             if pairCondition.eliminateDuplicatedPair:
#                 if pair in pairs:
#                     continue
#                 pairs.add(pair)
            
#             for key, l in tmp_lists.items():
#                 res_lists[key].append(l[i])
#             rest_length -= 1

#     return res_lists

# def genRandQueries(
#         queryConditions: "list[QueryCondition]",
#     ):
#     """
#     query_name = ${クエリ名}
#     c = PairCondition
#     """
#     res_queries = []
#     for queryCondition in queryConditions:
#         type = queryCondition.query_name
#         queries = genRandValPairsWithConditions(
#             pairCondition=queryCondition.pairCondition
#         )

#         for i in range(queryCondition.pairCondition.length):
#             query_line = [type]
#             for query in queries.values():
#                 query_line.append(str(query[i]))
#             res_queries.append(" ".join(query_line))

#     random.shuffle(res_queries)   
#     return res_queries

# def writeNums(file_handler, *args: int) -> None:
#     file_handler.write(" ".join(list(map(str, args))))
#     file_handler.write("\n")
#     return

# def writeLists(file_handler, *args: list, vertical = False, delimiter: str = " ") -> None:
#     if vertical:
#         if len(set([len(L) for L in args])) != 1:
#             raise Exception("[ERROR] lists must be same length.")
#         args = zip(*args)
#     for p in args:
#         file_handler.write(delimiter.join(list(map(str, p))))
#         file_handler.write("\n")
#     return


class QueryCondition():
    def __init__(self,
                 query_name: str,
                 pairCondition: PairCondition) -> None:
        """
        query_name = ${クエリ名}
        pairCondition = PairCondition
        """
        self.query_name = query_name
        self.pairCondition = pairCondition
        