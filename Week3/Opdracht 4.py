def makeWordsDict(text):
    words_dict = {}

    for line in text:
        for word in line.split(" "):
            word = word.strip("\n")
            word = word.strip(".")
            word = word.strip(",")
            word = word.strip("(")
            word = word.strip(")")
            word = word.strip("\'")
            word = word.strip("\"")
            word = word.strip("!")
            word = word.strip("?")
            word = word.strip(":")
            if word != "":
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1

    return words_dict

def dictToTxt(words_dict):
    text = open("dictFreq.txt", "w")
    for key in words_dict:
        text.write(key + " " + str(words_dict[key]) + "\n")
    text.close()

my_text = open("TextFile.txt", "r")
my_dict = makeWordsDict(my_text)
dictToTxt(my_dict)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

    def addWord(self, word):
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = TrieNode()
                current = current.children[char]
        current.value += 1

    def find(self, word):
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return 0
        return current.value

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        self.root.addWord(word)

    def find(self, word):
        return self.root.find(word)

def wordsToTrie(text):
    my_trie = Trie()
    for line in text:
        for word in line.split(" "):
            word = word.strip("\n")
            word = word.strip(".")
            word = word.strip(",")
            word = word.strip("(")
            word = word.strip(")")
            word = word.strip("\'")
            word = word.strip("\"")
            word = word.strip("!")
            word = word.strip("?")
            word = word.strip(":")
            if word != "":
                my_trie.addWord(word)
    return my_trie.root

def trieToTxt(trieNode, text, stringToWrite = ""):
    if trieNode.value > 0:
        text.write(stringToWrite + " " + str(trieNode.value) + "\n")
    if len(trieNode.children.keys()) > 0:
        for key in trieNode.children:
            trieToTxt(trieNode.children[key], text, stringToWrite + key)


my_second_text = open("TextFile.txt", "r")
my_trie_root = wordsToTrie(my_second_text)
trietext = open("trieFreq.txt", "w")
trieToTxt(my_trie_root, trietext)

def freqDict(text):
    my_dict = {}
    for line in text:
        word, freq = line.split(" ")
        my_dict[word] = freq
    return my_dict

dicttext = open("dictFreq.txt", "r")
dictFreq = freqDict(dicttext)
trietext = open("trieFreq.txt", "r")
trieFreq = freqDict(trietext)

def check2dicts(dict1, dict2):
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False
    for key in dict2:
        if dict2[key] != dict1[key]:
            return False
    return True

print(dictFreq.keys())
print(trieFreq.keys())
print(check2dicts(dictFreq, trieFreq))
