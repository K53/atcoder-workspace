a = 5
import math
decimalPart, integerPart = math.modf(math.log2(len(compressed.keys())))
seglen = 2 ** (int(integerPart) + 1)