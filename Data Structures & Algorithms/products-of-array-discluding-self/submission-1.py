class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                product = product * nums[j]
            res.append(product)
            product = 1
        return res
        
