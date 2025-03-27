def get_num_words(text):
    words = text.split()
    return len(words)

def letterCount(content):
    content_low = content.lower()
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'æ', 'â', 'ê', 'ë', 'ô']
    char_count = dict.fromkeys(alphabet,0) 
    for char in content_low:
        if char in alphabet:
            char_count[char] += 1
    return char_count

def sorted_char_list(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})

    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list
def print_report(text, path):
    num_words = get_num_words(text)
    num_chars = letterCount(text)
    sorted_chars = sorted_char_list(num_chars)
    print(f"Found {num_words} total words")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")