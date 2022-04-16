a = 5
import math
decimalPart, integerPart = math.modf(math.log2(a))
seglen = int(integerPart) + 1
