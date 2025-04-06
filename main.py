import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("------------ Word Count ---------")
    word_count = get_word_count(get_book_text(sys.argv[1]))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(get_book_text(sys.argv[1]))
    lst = sort_char(char_count)
    for i in lst:
        if i['character'].isalpha():
            print(f"{i['character']}: {i['count']}")
    print("============= END ===============")

main()
