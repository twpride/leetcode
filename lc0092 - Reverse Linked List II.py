class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        cur = head
        
        prev=None
        beg=None
        
        x=1
        
        while x<=n:
          if x+1 == m: 
            beg=cur
          if x==m:
            end=cur
            
          if x>=m:
            temp=cur.next  
            cur.next=prev
            prev=cur
            cur=temp
          else:
            cur=cur.next
            
          x+=1
          
        end.next=cur
        
        if beg:
          beg.next=prev
          return head
        
        return prev
