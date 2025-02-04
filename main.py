def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars_dict(text):
    text = text.lower()
    chars = {}

    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char, num in num_chars_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_num_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    for charnum in chars_sorted_list:
        if charnum["char"].isalpha():
            print(f"The '{charnum["char"]}' character was found {charnum["num"]} times")

    print("--- End report ---")

main()
