from pythonds.basic.deque import Deque


# class Deque:
#     def __init__(self):
#         self.items = []
#
#     def isEmty(self):
#         return self.items == []
#
#     def addFront(self, item):
#         self.items.append(item)
#
#     def addRear(self, item):
#         self.items.insert(0,item)
#
#     def removeFront(self):
#         return self.items.pop()
#
#     def removeRear(self):
#         return self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
#

def pal_checker(astring):
    char_deque = Deque()
    for ch in astring:
        char_deque.addRear(ch)
    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker('lsdkjfskl'))
#print(pal_checker("radaa"))