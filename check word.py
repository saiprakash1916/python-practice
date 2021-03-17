import re
sentence = str(input("Enter the sentence: "))
word = str(input("Enter the word: "))
if re.search(word,sentence):
    print(word, "is present in this sentence")
else:
    print(word, "is not present in this sentence")