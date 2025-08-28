import sys
from stats import get_number_words, get_count_characters, get_sorted_counts



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_number_words(book)
    count_characters = get_count_characters(book)
    sorted_characters = get_sorted_counts(count_characters)

    #Pretty Analysis
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_characters:
        print(f"{x['char']}: {x['num']}")
    print("============= END ===============")


main()
