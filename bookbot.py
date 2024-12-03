
def readFile():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordCount(content):
    counter = 0
    words = content.split(" ")
    return len(words)

def letterCount(content):
    alphabet = {'a': 0, 'b': 0, 'c': 0, 'd' : 0, 'e': 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i': 0, 'j' : 0, 'k' : 0, 'l': 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p': 0, 'q' : 0, 'r' : 0, 's': 0,'t' : 0, 'u' : 0, 'v': 0, 'w': 0, 'x': 0,'y': 0, 'z': 0} 
    lowerContent = content.lower()
    for letter in content:
        for letters in alphabet:
            if(letters == letter):
                alphabet[letters] += 1
    return alphabet
 


print(wordCount(readFile()))
print(letterCount(readFile()))
