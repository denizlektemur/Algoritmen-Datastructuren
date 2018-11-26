class mystack:
    def __init__(self, stackList = []):
        self.stack = stackList

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return  None

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

myNumbersStack = mystack()