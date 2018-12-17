from random import randint

class sepChainHash:
    def __init__(self, initialTableSize = 8):
        self.table = list()
        self.tableSize = initialTableSize
        self.amountOfElements = 0
        for i in range(self.tableSize):
            self.table.append(set())

    def indexFromElement(self, element):
        return hash(element) % self.tableSize

    def __repr__(self):
        return str(self.table)

    def isTooFull(self):
        if (self.amountOfElements / self.tableSize) > 0.75:
            return True
        return False

    def search(self, element):
        location = self.indexFromElement(element)
        if element in self.table[location]:
            return True
        return False

    def insert(self, element):
        location = self.indexFromElement(element)
        self.table[location].add(element)
        self.amountOfElements += 1
        if self.isTooFull():
            self.rehash(self.tableSize * 2)

    def delete(self, element):
        location = self.indexFromElement(element)
        if element in self.table[location]:
            self.table[location].remove(element)

    def rehash(self, newLen):
        oldElements = list()
        for subList in self.table:
            for element in subList:
                oldElements.append(element)
        self.table.clear()
        self.tableSize = newLen
        for i in range(self.tableSize):
            self.table.append(set())
        for element in oldElements:
            self.insert(element)
        print("Table has been rehashed\nNew Table:\n", str(self.table))

myChainHash = sepChainHash()
randomList = []
for i in range(200):
    randomNumber = randint(1,500)
    randomList.append(randomNumber*0.42)
for element in randomList:
    myChainHash.insert(element)
for i in range(100):
    myChainHash.delete(randomList.pop())
print("\nChainList after deletion:\n", myChainHash, "\n")
print("Expecting True:", myChainHash.search(randomList[-1]))
print("Expecting False:", myChainHash.search(10))