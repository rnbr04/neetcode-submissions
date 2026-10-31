# optimized prefix-suffix solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # build the prefix product array
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]


        # build the suffix product array over the prefix product array
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = postfix * res[i]
            postfix *= nums[i]

        
        return res

