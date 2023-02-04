# DPなどで出てくる任意次元の多次元配列でINFなどの初期値を空文字に置換して出力する。

def print_for_inf_replacable(l, replace_target):
    def _replace(l):
        if isinstance(l[0], list):
            return [_replace(ll) for ll in l]
        else:
            return ['' if i == replace_target else i for i in l]
    print(_replace(l))

# Usage
INF = 10 ** 16
d1 = [1,2,3,4,INF,5,INF,INF]
print_for_inf_replacable(d1, replace_target=INF) 
# [1, 2, 3, 4, '', 5, '', '']

d2 = [d1, d1]
print_for_inf_replacable(d2, replace_target=INF) 
# [[1, 2, 3, 4, '', 5, '', ''], [1, 2, 3, 4, '', 5, '', '']]

d3 = [d2, d2]
print_for_inf_replacable(d3, replace_target=INF) 
# [[[1, 2, 3, 4, '', 5, '', ''], [1, 2, 3, 4, '', 5, '', '']], [[1, 2, 3, 4, '', 5, '', ''], [1, 2, 3, 4, '', 5, '', '']]]
