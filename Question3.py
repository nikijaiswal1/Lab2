sentence = input(" Enter your sentence: ")
words = sentence.split()
used = []
i = 0
while i < len(words): 
    if words[i] not in used:
        count = 0
        j = 0
        while j < len(words):
            if words[i] == words[j]:
                count += 1
            j += 1
        print(words[i], count)
        used.append(words[i])
    i += 1