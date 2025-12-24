from stats import word_count, char_count, sort_count, count_sort
import sys

if len(sys.argv) == 2:
    input_file = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
    return file_contents


print("Found " + str(word_count(get_book_text(input_file))) + " total words")

char_count = sort_count(char_count(input_file))

for i in char_count:
    print(i["char"] + ": " + str(i["num"]))
