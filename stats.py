def word_count(filepath):
    total_count = len(filepath.split())
    return total_count

def char_count(filepath):
    with open(filepath) as book:
        lowercase_book = book.read().lower()
        counted_chars = {}
        for i in range(0,len(lowercase_book)):
            if lowercase_book[i] not in counted_chars:
                counted_chars[lowercase_book[i]] = 0
            counted_chars[lowercase_book[i]] += 1
    return counted_chars

def sort_count(count_to_sort):
    sorted_dicts = []
    for char in count_to_sort:
        sorted_dicts.append({"char":char.strip("'"),"num":count_to_sort[char]})
    sorted_dicts.sort(reverse=True,key=count_sort)
    return sorted_dicts

def count_sort(count_list):
    return count_list["num"]
