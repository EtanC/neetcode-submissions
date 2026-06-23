class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # can do brute force 
        # how this works, is two loops 

        result = []
        def backtrack(start, path): 
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result