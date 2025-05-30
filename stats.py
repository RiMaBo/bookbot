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
