#
# 206. Reverse Linked List
# Reverse a singly linked list.
#

import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

def display(lst):
    if lst:
        print(lst.val, end='->')
        display(lst.next)
    else:
        print('')

def main():
    s = Solution()
    lst = ListNode('a')
    nodeb = ListNode('b')
    nodec = ListNode('c')
    noded = ListNode('d')
    lst.next = nodeb
    nodeb.next = nodec
    nodec.next = noded

    display(lst)
    result = s.reverseList(lst)
    display(result)


if __name__ == '__main__':
    main()
