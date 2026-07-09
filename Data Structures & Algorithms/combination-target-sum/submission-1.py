class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # same thing as subset 

        # dfs 
        # base case is when the sum of current array = target, append, if greater, backtrack to last
        # what i dont get is the condition to choose itself, unlike subset where you can only choose number once
        res: list[list[int]] = []

        def dfs(i, current, total): 
            if total == target: 
                res.append(current[:])
                return 
            if total > target or i >= len(nums):
                return 
        
            current.append(nums[i])
            dfs(i, current, total + nums[i])
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return res