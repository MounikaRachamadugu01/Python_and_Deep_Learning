f = open("WordCount.txt", 'r')
wordcount = {}
for line in f.read().split():
    word = line.lower()
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
print("Output written to file to output.txt")
print(wordcount, file=open("output.txt", "w"))