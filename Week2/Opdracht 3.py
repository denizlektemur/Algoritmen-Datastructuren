class mystack:
    def __init__(self, list = []):
        self.stack = list

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

def check_string(myString):
    stack = mystack()
    mypairs = {'>' : '<', ']' : '[', ')' : '('}
    if len(myString) > 0:
        for character in myString:
            if character == '<' or character == '[' or character == '(':
                stack.push(character)
            if character == '>' or character == ']' or character == ')':
                if(stack.peek() == mypairs.get(character)):
                    stack.pop()
                else:
                    return False
        if stack.peek() != None:
            return False
    return True

print(check_string('((<>)())'))
print(check_string('[(<>)]()(()())'))
print(check_string('((<>))'))
print(check_string('([)]'))
print(check_string('(((<)>))'))
print(check_string('((<>())'))