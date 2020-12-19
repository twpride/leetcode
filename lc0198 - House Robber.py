class Solution:
  def rob(self, nums: List[int]) -> int:
    mem =[-1]*len(nums)

    def fcn(idx):
      if idx<0: return 0
      if mem[idx]>=0: return mem[idx]
      else:
        mem[idx] = max(nums[idx] + fcn(idx-2), fcn(idx-1))
        return mem[idx]


    return fcn(len(nums)-1)