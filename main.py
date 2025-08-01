import sys
from stats import word_count, character_count, create_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():

    text = get_book_text(filepath)
    num_characters = character_count(text)
    num_words = word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_chars = create_sorted_list(num_characters)
    for char in list_of_chars:
        if char['char'].isalpha():
            print(char['char'] + ': ' + str(char['num']))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
