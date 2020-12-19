class Solution: # sorting
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()

        ans=0
        strk=1
        for i in range(1,len(nums)):
          if nums[i]-nums[i-1]==0: continue
          if nums[i]-nums[i-1]==1:
            strk+=1
          else:
            ans=max(ans,strk)
            strk=1
            
        ans=max(ans,strk)
        return ans
      
      
      
# class Solution: # hashset
#     def longestConsecutive(self, nums: List[int]) -> int:
#         snums=set(nums)
#         ans=0
#         for i in nums:
#           if i-1 in snums: pass
#           else:
#             j=i
#             while j+1 in snums:
#               j+=1
#             ans= max(j-i+1,ans)
#         return ans