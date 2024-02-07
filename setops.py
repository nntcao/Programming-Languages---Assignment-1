
def delimiter_helper_get_word(string, symbol):
    if not string or string[0] == symbol:
        return ""
    return string[0] + delimiter_helper_get_word(string[1:], symbol)


def delimiter_helper_next(string, symbol):
    if not string:
        return []
    if len(string) > 1 and string[0] == symbol and string[1] != symbol:
        return [delimiter_helper_get_word(string[1:], symbol)] + delimiter_helper_next(string[1:], symbol)
    return delimiter_helper_next(string[1:], symbol)


def delimiter(string, symbol):
    if not string:
        return []
    if string[0] != symbol:
        return [delimiter_helper_get_word(string[0:], symbol)] + delimiter_helper_next(string[1:], symbol)
    return delimiter_helper_next(string[1:], symbol)


def remove_symbol(string, symbol):
    if not string:
        return ""
    if string[0] == symbol:
        return remove_symbol(string[1:], symbol)
    return string[0] + remove_symbol(string[1:], symbol)


def remove_symbols(string, symbols):
    if not symbols:
        return string
    return remove_symbols(remove_symbol(string, symbols[0]), symbols[1:])


def to_lower(string):
    if not string:
        return ""
    if 65 <= ord(string[0]) and ord(string[0]) <= 90:
        return chr(ord(string[0]) + 32) + to_lower(string[1:])
    return string[0] + to_lower(string[1:])

# checks if element exists in list l


def exists(l, element):
    if not l:
        return False
    if l[0] == element:
        return True
    return exists(l[1:], element)


def replace_symbol(string, old_symbol, new_symbol):
    if not string:
        return ""
    if string[0] == old_symbol:
        return new_symbol + replace_symbol(string[1:], old_symbol, new_symbol)
    return string[0] + replace_symbol(string[1:], old_symbol, new_symbol)


# returns list l with only unique values
# currently O(n^2)
def unique(l):
    if not l:
        return []
    if exists(l[1:], l[0]):
        return unique(l[1:])
    return [l[0]] + unique(l[1:])


def unique_given_sorted_helper(sorted_list, curr_el):
    if not sorted_list:
        return []
    if sorted_list == curr_el:
        return unique_given_sorted_helper(sorted_list[1:], curr_el)
    return [sorted_list[0]] + unique_given_sorted_helper(sorted_list[1:], sorted_list[0])

# returns list l with only unique values, assuming list l is sorted
# optimized time complexity: O(n) instead of O(n^2)
def unique_given_sorted(sorted_list):
    if not sorted_list:
        return []
    return [sorted_list[0]] + unique_given_sorted_helper(sorted_list[1:], sorted_list[0])


def text_input_to_sorted_word_set(string):
    # expanded for readability---lovely scheme-esque formatting :)

    # removes punctuation, replaces \t and \n with spaces so that the delimiter can capture all words, then sets all words to lowercase
    # afterwards, sorts the list of words, then removes elements for a unique list
    return unique_given_sorted(
        sort(
            list(
                map(
                    to_lower,
                    delimiter(
                        replace_symbol(
                            replace_symbol(
                                remove_symbols(
                                    string,
                                    ["!", "?", "'", "\"", ".", ",",
                                     "/", "\\", "~", "-", "(", ")"]
                                ),
                                "\n",
                                " "
                            ),
                            "\t",
                            " "
                        ),
                        " "
                    )
                )
            )
        )
    )


def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    return [l2[0]] + merge(l1, l2[1:])


def merge_sort(l):
    if len(l) == 1:
        return l
    return merge(merge_sort(l[0:len(l)//2]), merge_sort(l[len(l)//2:]))

# sort list l ascending order using merge sort
def sort(l):
    return merge_sort(l)

# assumes sorted ordered set
def difference_given_sorted_helper(set_1, set_2):
    if not set_1:
        return set_2
    if not set_2:
        return set_1
    if set_1[0] == set_2[0]:
        return difference_given_sorted_helper(set_1[1:], set_2[1:])
    if set_1[0] < set_2[0]:
        return [set_1[0]] + difference_given_sorted_helper(set_1[1:], set_2)
    return [set_2[0]] + difference_given_sorted_helper(set_1, set_2[1:])

def difference_given_sorted(set_1, set_2):
    return sort(difference_given_sorted_helper(set_1, set_2))

# assumes sorted ordered set
def union_given_sorted(set_1, set_2):
    return unique_given_sorted(sort(set_1 + set_2))

# assumes sorted ordered set
def intersection_given_sorted_helper(set_1, set_2):
    if not set_1 or not set_2:
        return []
    if set_1[0] == set_2[0]:
        return [set_1[0]] + intersection_given_sorted_helper(set_1[1:], set_2[1:])
    if set_1[0] < set_2[0]:
        return intersection_given_sorted_helper(set_1[1:], set_2)
    return intersection_given_sorted_helper(set_1, set_2[1:])

def intersection_given_sorted(set_1, set_2):
    return sort(intersection_given_sorted_helper(set_1, set_2))

def main():

    # file and sys I/O
    filepath_1 = "./test/a.txt"
    filepath_2 = "./test/b.txt"

    file1 = open(filepath_1)
    text1 = file1.read()

    file2 = open(filepath_2)
    text2 = file2.read()

    file1.close()
    file2.close()

    # operations
    sorted_word_set_1 = text_input_to_sorted_word_set(text1)
    sorted_word_set_2 = text_input_to_sorted_word_set(text2)
    print(sorted_word_set_1)
    print(sorted_word_set_2)

    print(difference_given_sorted(sorted_word_set_1, sorted_word_set_2))
    print(union_given_sorted(sorted_word_set_1, sorted_word_set_2))
    print(intersection_given_sorted(sorted_word_set_1, sorted_word_set_2))


if __name__ == "__main__":
    main()
