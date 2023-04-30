
# 高速化の方法
# http://cielavenir.github.io/blog/2017/10/23/inn-reservation/


def scheduling(brackets: "list[int, int]", slotsize: int = 1):
    """
    brackets: ("end time", "begin time")
    slotsize: 区間内で重複を許す個数。(一度に並列実行できるタスク数。)
    """
    brackets = sorted(brackets)
    ans = []
    slots = [-1] * slotsize
    for end_time, begin_time in brackets:
        # 開始点の時点で終了しているタスクがスロットに含まれるなら、それを差し替える。
        already_done_tasks = [s for s in slots if s < begin_time]
        if len(already_done_tasks) != 0:
            slots[slots.index(max(already_done_tasks))] = end_time # slotsの検索はO(len(slots))かかる。高速化するならmultisetを使う。
            ans.append((end_time, begin_time))
    return ans



print(scheduling([
    (5, 1),
    (6, 4),
    (8, 6)
])) # -> [(5, 1), (8, 6)] # 1番目と3番目のタスクが採用された。
