file_object = open("AI.txt", "r")

words = file_object.readline()
words = words.lower()

unwanted_char = ['.', ',', "(", ")", '"', "%", "'", ";", ":"]
unwanted_char = str(unwanted_char)


wordfreq = {}

for x in unwanted_char:
    words = words.replace(x,' ')
words = words.split()


wordlist = []
for i in words:
    wordlist.append(i)

for word in words:
    if word in wordfreq:
        counter = wordlist.count(word)
        wordfreq[word] = counter
    else:
        wordfreq[word] = 1

for key in list(wordfreq.keys()):
    print(key, ": ", wordfreq[key], sep='')
   

file_object.close()