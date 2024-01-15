from typing import Optional

import ListNode

'''
82. Remove Duplicates from Sorted List II
Compare the val of cur.next and cur.next.next
If they are equal, skip the node equal to cur.next.val.
And cur.next point to the node not equal to cur.next.val.
If they are not equal, cur = cur.next.
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
