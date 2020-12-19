class Solution:


'''

we use helper fcn recursively search array, we search from end (arbitrary choice)
memo can either be -1: not searched yet, >=0: searched

'''
  def rb(self, nums: List[int]) -> int:
    mem =[-1]*len(nums)

    def fcn(idx):
      if idx<0: return 0
      if mem[idx]>=0: return mem[idx]
      else:
        mem[idx] = max(nums[idx] + fcn(idx-2), fcn(idx-1))
        return mem[idx]


    return fcn(len(nums)-1)
  
  def rob(self, nums: List[int]) -> int:
    n=len(nums)
    
    if n<=3: return max(nums)
    
    return max(self.rb(nums[:-1]),self.rb(nums[1:]))