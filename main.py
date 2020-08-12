class Node:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def getNextNode(self, node: Node) -> int:
    if node == None or node.next == None:
      return None

    return node.next

  def getNodeVal(self, node: Node) -> int:
    if node == None or node.val == None:
      return 0

    return node.val

  def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
    lStart = None
    lEnd = None

    one = l1
    two = l2
    addition = 0

    while one != None or two != None or addition != 0:
      sum = self.getNodeVal(one) + self.getNodeVal(two) + addition
      addition = 0

      if sum > 9:
        sum = sum % 10
        addition = 1

      if lStart == None:
        lStart = Node(sum)
        lEnd = lStart
      else:
        lEnd.next = Node(sum)
        lEnd = lEnd.next

      one, two = self.getNextNode(one), self.getNextNode(two)

    return lStart


my = Solution()

l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))

# l1 = Node()
# l2 = Node()

lAns = my.addTwoNumbers(l1, l2)

while lAns != None:
  print(lAns.val)
  lAns = lAns.next

print('end')

# +
# 2 4 3
# 5 6 4

#   1
# 7 0 8

# +
# 1
# 9 9 9

# 1 1 1
# 0 0 0 1

# Results:
# Runtime: 68 ms, faster than 92.49% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.8 MB, less than 79.88% of Python3 online submissions for Add Two Numbers.