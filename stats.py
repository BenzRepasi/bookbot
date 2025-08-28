def get_number_words(book):
    book_set = book.split()
    return len(book_set)

def get_count_characters(book):
    count_dict = {}
    book = book.lower()
    for character in book:
        if character in count_dict :
            count_dict[character] +=1
        else:
            count_dict[character] = 1
    return count_dict

def sort_num(item):
    return item["num"]

def get_sorted_counts(counts):
    list_of_counts = []
    for character, count in counts.items():
        if character.isalpha():
            list_of_counts.append({"char": character, "num": count})
    list_of_counts.sort(reverse=True, key=sort_num)
    return list_of_counts