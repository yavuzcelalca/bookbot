
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    start_text = f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n\n"
    end_text = "\n--- End report ---"
    empty_string = ""
    num_characters.sort(reverse=True, key=sort_on)
    for i in num_characters:
        empty_string = empty_string + f"\nThe '{i['char']}' character was found {i['num']} times"
    empty_string = start_text + empty_string + end_text
    print(empty_string)


def sort_on(dict_item):
    return dict_item["num"]



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_list = []
    text = text.lower()
    empty_dic = {}
    for i in text:
        if i.isalpha():
            if i not in empty_dic:
                empty_dic[i] = 1
            else:
                empty_dic[i] += 1
    for char,count in empty_dic.items():
        char_list.append({"char":char, "num": count})
    return char_list


if __name__ == "__main__":
    main()