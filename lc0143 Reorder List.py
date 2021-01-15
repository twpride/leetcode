# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

  def reorderList(self, head: ListNode) -> None:
    """
        Do not return anything, modify head in-place instead.
        """
    if not head:
      return head

    slow = fast = head

    # find median node, or upper median
    while fast.next and fast.next.next:
      fast = fast.next.next
      slow = slow.next

    mid = slow.next  # start of second half
    slow.next = None  # break first from second half

    prev = None
    cur = mid
    while cur:
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp

    main = head  # pointer to main list to be merged into
    side = prev  # pointer to side list to be merged

    while side:
      temp = main.next
      main.next = side
      side = temp
      main = main.next
