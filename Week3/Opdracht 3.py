class BSTNode:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self, nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' ' * nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def max(self):
        while self.right != None:
            self = self.right
        return self.element

    def rsearch(self, e):
        if self.element == e:
            return self
        if self.left:
            if self.left.rsearch(e):
                return self.left.rsearch(e)
        if self.right:
            if self.right.rsearch(e):
                return self.right.rsearch(e)
        return None

    def rinsert(self, e):
        if e > self.element:
            if not self.right:
                self.right = BSTNode(e, None, None)
            else:
                self.right.rinsert(e)
        elif e < self.element:
            if not self.left:
                self.left = BSTNode(e, None, None)
            else:
                self.left.rinsert(e)
        else:
            return None

    def showLevelOrder(self):
        currentLevel = [self]
        while currentLevel:
            nextLevel = []
            for node in currentLevel:
                print(node.element, end = ' ')
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            print("\n")
            currentLevel = nextLevel

    def insert(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)
        return not found

    def insertArray(self, a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a) - 1
        mid = (low + high + 1) // 2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a, low, mid - 1)
        if high > mid:
            self.insertArray(a, mid + 1, high)

    def search(self, e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def search2(self, e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left;
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None

    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self, e):
        parent = self.getParent(e);

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True


class BST:
    def __init__(self, a=None):
        if a:
            mid = len(a) // 2
            self.root = BSTNode(a[mid], None, None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid + 1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def max(self):
        if self.root.element != None:
            return self.root.max()
        return "null-tree"

    def rsearch(self, e):
        if self.root and e:
            return self.root.rsearch(e)
        return None

    def rinsert(self, e):
        if e:
            if self.root:
                self.root.rinsert(e)
            else:
                self.root = BSTNode(e, None, None)
        else:
            return None

    def showLevelOrder(self):
        if self.root:
            self.root.showLevelOrder()
        else:
            return None

    def search(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def insert(self, e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False

    def delete(self, e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree();
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False

a = BST()
b = BST()
b.insert(8)
b.insert(89)
b.insert(5)
b.insert(15)
b.insert(22)
b.insert(9)
b.insert(4)
b.insert(1)
b.insert(2)
b.insert(15)

a.rinsert(8)
a.rinsert(89)
a.rinsert(5)
a.rinsert(15)
a.rinsert(22)
a.rinsert(9)
a.rinsert(4)
a.rinsert(1)
a.rinsert(2)
a.rinsert(15)

print(b)
print(a)

a.showLevelOrder()

print("maximum =",a.max(), "\n")
print(a.rsearch(15))
print(a.search(15))
print('----------------')
