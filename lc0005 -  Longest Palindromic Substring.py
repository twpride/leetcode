class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def ispal(lo,hi):
            while lo-1>=0 and hi+1<len(s) and s[lo-1]==s[hi+1]:
                lo-=1
                hi+=1
            return s[lo:hi+1]
        
        best=1
        ans=s[0]
        for i in range(len(s)):
            cur = ispal(i,i)
            if len(cur)>len(ans): 
              ans=cur
            cur = ispal(i+1,i)
            if len(cur)>len(ans):
              ans=cur

        return ans