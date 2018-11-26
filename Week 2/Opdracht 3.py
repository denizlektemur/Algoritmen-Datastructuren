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

def check_string(string):
    stack = mystack()
    mypairs = {'>' : '<', ']' : '[', ')' : '('}
    if len(string) > 0:
        for i in string:
            if i == '<' or i == '[' or i == '(':
                stack.push(i)
            if i == '>' or i == ']' or i == ')':
                if(stack.peek() == mypairs.get(i)):
                    stack.pop()
                else:
                    return False
        return True
    return True

print(check_string('((<>)())'))
print(check_string('[(<>)]()(()())'))
print(check_string('((<>))'))
print(check_string('([)]'))
print(check_string('(((<)>))'))