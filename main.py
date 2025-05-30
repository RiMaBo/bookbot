from stats import get_num_words
from stats import get_num_chars_dict
from stats import chars_dict_to_sorted_list
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_num_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars_dict)

    # print(f"--- Begin report of {book_path} ---")
    # print(f"{num_words} words found in the document")
    # print("")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for charnum in chars_sorted_list:
        if charnum["char"].isalpha():
            # print(f"The '{charnum["char"]}' character was found {charnum["num"]} times")
            # print(f"'{charnum["char"]}': {charnum["num"]}")
            print(f"{charnum["char"]}: {charnum["num"]}")

    # print("--- End report ---")
    print("============= END ===============")


main()
