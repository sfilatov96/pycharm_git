# Definition for singly-linked list.



class ListNode:
    def __str__(self):
        return f'val -- {self.val}'
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, l: ListNode):
        prev = None
        while l:
            curr = l.next
            l.next = prev
            prev = l
            l = curr

        return prev

    def _calculate(self, l: ListNode, grd=1):
        if not l:
            return 0
        res = self._calculate(l.next, grd=grd*10)
        return (l.val*grd) + res

    def calculate(self, num):
        val = num % 10
        next_ = int(num / 10)
        if next_ == 0:
            r = None
        else:
            r = self.calculate(next_)
        return ListNode(val=val, next=r)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_ = self._calculate(l1) + self._calculate(l2)
        return self.calculate(sum_)


if __name__ == "__main__":
    l1 = ListNode(val=0)
    Solution().addTwoNumbers(l1, l1)
