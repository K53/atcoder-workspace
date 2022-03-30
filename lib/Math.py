# ------------------------------------------------------------------------------
#     2次元配列回転
# ------------------------------------------------------------------------------
# - verify
#   - https://atcoder.jp/contests/abc107/tasks/abc107_b (時計・反時計)
# ------------------------------------------------------------------------------


original = [
    ('1', '2', '3'), 
    ('8', '9', '4'), 
    ('7', '6', '5')
]

# 90度時計回り回転 (+90)
clockwiseRotated = list(zip(*original[::-1]))
print(clockwiseRotated)
"""
[
    ('7', '8', '1'), 
    ('6', '9', '2'), 
    ('5', '4', '3')
]
"""

# 90度反時計回り回転 (+270)
counterClocwiseRotate = list(zip(*[o[::-1] for o in original]))
"""
[
    ('3', '4', '5'), 
    ('2', '9', '6'), 
    ('1', '8', '7')
]
"""
print(counterClocwiseRotate)

# 180度回転
rotated180 = [o[::-1] for o in original][::-1]
print(rotated180)
"""
[
    ('5', '6', '7'), 
    ('4', '9', '8'), 
    ('3', '2', '1')
]
"""

# 左右反転
flipHorizontal = [o[::-1] for o in original]
print(flipHorizontal)
"""
[
    ('3', '2', '1'), 
    ('4', '9', '8'), 
    ('5', '6', '7')
]
"""

# 上下反転
flipVertical = [o for o in original][::-1]
"""
[
    ('7', '6', '5'), 
    ('8', '9', '4'), 
    ('1', '2', '3')
]
"""
print(flipVertical)