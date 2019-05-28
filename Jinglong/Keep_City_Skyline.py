class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        tb, lr = [None] * len(grid), [None] * len(grid)
        old_skyline = 0
        for r, row in enumerate(grid):
            lr[r] = max(row)
            old_skyline += sum(row)
        for c in range(len(grid)):
            tb[c] = max([v[c] for v in grid])
        descartes = [min(vr, vc) for vr in lr for vc in tb]
        new_skyline = sum(descartes)
        return new_skyline - old_skyline
