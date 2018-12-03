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
            if word.__hash__() in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word.__hash__()] = word
                words_dict[word] = 1

    return words_dict

my_text = open("TextFile.txt", "r")
my_dict = makeWordsDict(my_text)
print("The word \"the\" occurs", my_dict["the"], "times")

