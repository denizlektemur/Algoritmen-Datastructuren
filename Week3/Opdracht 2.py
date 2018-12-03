class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        if current != None:
            s = s + str(current)
            current = self.tail.next
        while current != self.tail:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.tail: # self.tail == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e,self.tail.next)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self, e):
        if self.tail:
            current = self.tail
            if self.tail.data == e:
                if current.next == self.tail:
                    self.tail = None
                else:
                    while current.next.next != self.tail:
                        current = current.next
                    current.next.next = self.tail.next
                    self.tail = current.next
                    return
            while current.next != self.tail:
                if current.next.data == e:
                    current.next = current.next.next
                    return
                current = current.next

print("///////////////////////////////\nTAIL IS PRINTED AS FIRST NUMBER\n///////////////////////////////\n")
mylist = MyLinkedList()
print(mylist)
mylist.addLast(5)
print(mylist)
mylist.delete(5)
print(mylist)
mylist.addLast(3)
mylist.addLast(2)
mylist.addLast(15)
mylist.addLast(69)
print(mylist)
mylist.delete(69)
print(mylist)
mylist.delete(55)
print(mylist)