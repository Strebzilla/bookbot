import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def print_report(path, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")    
    for character in character_count:
        if character["character"].isalpha():
            
            print(f"{character["character"]}: {character["count"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    text = get_book_text(book_path)    
    print_report(book_path, count_words(text), sort_chars(count_chars(text)))

main()