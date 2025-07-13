def find_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    used_vowels = set()
    for char in sentence.lower():
        if char in vowels:
            used_vowels.add(char)
    return used_vowels

text = input("Enter a sentence: ")
result = find_vowels(text)
print("Unique vowels used:", result) 