
class Solution:
    def reorderList(self, head):
        phead = head
        def f(head, phead):
            if head.next == None:
                return phead
            t = f(head.next, phead)
            if t == None or t.next == None or t == head:
                return None
            bk = t.next
            t.next = head.next
            head.next = None
            t.next.next = bk
            return t.next.next
        f(head, phead)
        
                
