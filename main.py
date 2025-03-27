import sys
from stats import print_report
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print_report(text, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
