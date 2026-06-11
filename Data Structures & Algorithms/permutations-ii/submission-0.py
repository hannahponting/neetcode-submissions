class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visit = [False] * n
        perm = []

        nums.sort()

        def backtrack():
            if len(perm) == n:
                res.append(perm[:])
                return

            for j in range(n):
                if visit[j]:
                    continue

                # duplicate pruning
                if j > 0 and nums[j] == nums[j - 1] and not visit[j - 1]:
                    continue

                visit[j] = True
                perm.append(nums[j])

                backtrack()

                perm.pop()
                visit[j] = False

        backtrack()
        return res