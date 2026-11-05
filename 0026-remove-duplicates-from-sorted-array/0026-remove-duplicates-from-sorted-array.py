class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        j=1
        count=1
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1

            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
                count+=1

        return count
                
            
        