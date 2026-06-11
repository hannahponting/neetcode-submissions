class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1]*(len(nums)+1)
        post = [1]*(len(nums)+1)
        res = [0]*len(nums)

        for i in range(len(nums)-1, 0, -1):
            post[i-1] = post[i] * nums[i]
        post = post[:-1]

        for i in range(len(nums)):
            pre[i+1] = pre[i] * nums[i]
            res[i] = pre[i] * post[i]
        
        return res



    

