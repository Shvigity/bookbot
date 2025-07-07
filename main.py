from stats import word_count, char_count, char_sort, get_book_text
import sys

def main():
    if sys.argv[1:]:
        book_path = sys.argv[1]
        
        print("========= BOOKBOT =========")
        whole_document = get_book_text(book_path)
        
        word_count(whole_document)
        
        all_characters = char_count(whole_document)
        
        sorted_chars = char_sort(all_characters)
        for char in sorted_chars:
            print(f"{char['char']}: {char['num']}")

        return

    else:
        print("No book path provided. Please provide a path to a book file.")
        print("Usage: python main.py <path_to_book>")
        return 1

    

main()

