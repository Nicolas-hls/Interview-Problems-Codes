class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =  len(nums)
        total = n*(n+1) // 2
        return total - sum(nums)


#################
###  Testing  ###
#################

nums=[0,4,2,3,6,1]
print (Solution().missingNumber(nums))
