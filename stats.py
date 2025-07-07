def get_book_text(book_path):
    print(f"Analyzing book found at {book_path}...")
    with open(book_path, "r", encoding="utf-8") as file:
        document = file.read()

    return document

def word_count(document):
    print("--------- Word Count ---------")
    words = document.split()

    return print(f"Found {len(words)} total words")


def char_count(document): 
    all_chars = {}
    
    print("------ Character Count -------")
    all_chars_lower = document.lower()

    for char in all_chars_lower:
        if char in all_chars:
            all_chars[char] += 1
        else:
            all_chars.update({char: 1})

    return all_chars
    
def sort_on(items):
    return items["num"]

def char_sort(dictionary):
    list_of_dicts = []

    for item in dictionary:
       if item.isalpha():
            list_of_dicts.append({"char": item, "num": dictionary[item]})
            # print(f"{item}: {new_dict['num']}")
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    #list_of_dicts.sort(key=lambda x: x['num'], reverse=True)

    return list_of_dicts