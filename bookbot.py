
def readFile():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordCount(content):
    counter = 0
    words = content.split(" ")
    return len(words)




print(wordCount(readFile()))
