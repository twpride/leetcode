import heapq
class MedianFinder: # 2 heaps O(log(n))

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap=[] # store lower half
        self.minheap=[] # store upper half


    def addNum(self, num: int) -> None:
      
      #push to lower half
      heapq.heappush(self.maxheap,-num) # heapq default is a minheap
      
      #rebalance tree 
      heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
  
      # above 2 combined
      # heapq.heappush(self.minheap,-heapq.heappushpop(self.maxheap,-num))
      
      if len(self.minheap) > len(self.maxheap): #make sure lower half will always have 0 or 1 more element
        heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
        
        
    def findMedian(self) -> float:
      minheapl = len(self.minheap)
      maxheapl = len(self.maxheap)

      if maxheapl == minheapl:
        return (self.minheap[0]-self.maxheap[0])/2
      else:
        return -self.maxheap[0]

import bisect

class MedianFinder: # sorting O(n)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store=[]
        

    def addNum(self, num: int) -> None:
      # find leftmost num
      # this algo finds leftmost because when ele==num
      # algo select left half to keep
      # lo=0
      # hi = len(self.store)  # choice of len-1 will result in left median when even
      # while lo<hi:
      #   mid = lo+(hi-lo)//2
      #   if self.store[mid]<num:
      #     lo=mid+1
      #   else:
      #     hi=mid
      # it has to be mid+1 amd mid becuase when hi-lo==1, mid==lo
      
      lo=bisect.bisect_left(self.store,num,0,len(self.store)) #O(log(n))
      self.store.insert(lo,num) # O(n)

    def findMedian(self) -> float:
      storelen= len(self.store)
      if storelen==0:
        return None
      elif storelen==1:
        return self.store[0]
      elif storelen==2:
        return sum(self.store)/2
      if storelen %2 ==0:
        return sum(self.store[storelen//2-1:storelen//2+1])/2
      else:
        return self.store[storelen//2]
        