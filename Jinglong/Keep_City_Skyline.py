class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        tb, lr = [None] * len(grid), [None] * len(grid)
        old_skyline = 0
        for ind, row in enumerate(grid):
            lr[ind] = max(row)
            tb[ind] = max([v[ind] for v in grid])
            old_skyline += sum(row)
        descartes = [min(vr, vc) for vr in lr for vc in tb]
        new_skyline = sum(descartes)
        return new_skyline - old_skyline
