
def _delimiter_helper_get_word(string, symbol):
    if not string or string[0] == symbol:
        return ""
    return string[0] + _delimiter_helper_get_word(string[1:], symbol)


def _delimiter_helper_next(string, symbol):
    if not string:
        return []
    if len(string) > 1 and string[0] == symbol and string[1] != symbol:
        return [_delimiter_helper_get_word(string[1:], symbol)] + _delimiter_helper_next(string[1:], symbol)
    return _delimiter_helper_next(string[1:], symbol)


def delimiter(string, symbol):
    if not string:
        return []
    return _delimiter_helper_next(symbol + string, symbol)


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
def linear_search(l, element):
    if not l:
        return False
    if l[0] == element:
        return True
    return linear_search(l[1:], element)


def binary_search(l, element):
    if not l:
        return False
    if l[len(l) // 2] == element:
        return True
    if l[len(l) // 2] < element:
        return binary_search(l[len(l) // 2 + 1:], element)
    return binary_search(l[:len(l) // 2], element)


def replace_symbol(string, old_symbol, new_symbol):
    if not string:
        return ""
    if string[0] == old_symbol:
        return new_symbol + replace_symbol(string[1:], old_symbol, new_symbol)
    return string[0] + replace_symbol(string[1:], old_symbol, new_symbol)


def _unique_helper(sorted_list, curr_el):
    if not sorted_list:
        return []
    if sorted_list[0] == curr_el:
        return _unique_helper(sorted_list[1:], curr_el)
    return [sorted_list[0]] + _unique_helper(sorted_list[1:], sorted_list[0])

# returns list l with only unique values, assuming list l is sorted
# optimized time complexity: O(n) instead of O(n^2)
def unique(sorted_list):
    if not sorted_list:
        return []
    return [sorted_list[0]] + _unique_helper(sorted_list[1:], sorted_list[0])


def _merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1[0] <= l2[0]:
        return [l1[0]] + _merge(l1[1:], l2)
    return [l2[0]] + _merge(l1, l2[1:])


def _merge_sort(l):
    if len(l) <= 1:
        return l
    return _merge(_merge_sort(l[0:len(l)//2]), _merge_sort(l[len(l)//2:]))

# sort list l ascending order using merge sort
def sort(l):
    return _merge_sort(l)


def _difference_helper(sorted_set_1, sorted_set_2):
    if not sorted_set_1:
        return sorted_set_2
    if not sorted_set_2:
        return sorted_set_1
    if sorted_set_1[0] == sorted_set_2[0]:
        return _difference_helper(sorted_set_1[1:], sorted_set_2[1:])
    if sorted_set_1[0] < sorted_set_2[0]:
        return [sorted_set_1[0]] + _difference_helper(sorted_set_1[1:], sorted_set_2)
    return [sorted_set_2[0]] + _difference_helper(sorted_set_1, sorted_set_2[1:])

# assumes sorted ordered sets
def difference(sorted_set_1, sorted_set_2):
    return sort(_difference_helper(sorted_set_1, sorted_set_2))

# assumes sorted ordered sets
def union(sorted_set_1, sorted_set_2):
    return unique(sort(sorted_set_1 + sorted_set_2))


def _intersection_helper(sorted_set_1, sorted_set_2):
    if not sorted_set_1 or not sorted_set_2:
        return []
    if sorted_set_1[0] == sorted_set_2[0]:
        return [sorted_set_1[0]] + _intersection_helper(sorted_set_1[1:], sorted_set_2[1:])
    if sorted_set_1[0] < sorted_set_2[0]:
        return _intersection_helper(sorted_set_1[1:], sorted_set_2)
    return _intersection_helper(sorted_set_1, sorted_set_2[1:])

# assumes sorted ordered sets
def intersection(sorted_set_1, sorted_set_2):
    return sort(_intersection_helper(sorted_set_1, sorted_set_2))


def text_input_to_sorted_word_set(string):
    # expanded for readability---lovely scheme-esque formatting :)

    # removes punctuation, replaces \t and \n with spaces so that the delimiter can capture all words, then sets all words to lowercase
    # afterwards, sorts the list of words, then removes elements for a unique list
    return unique(
        sort(
            list(
                map(
                    to_lower,
                    delimiter(
                        replace_symbol(
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
                            "\r", 
                            " "
                        ),
                        " "
                    )
                )
            )
        )
    )


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

    print(difference(sorted_word_set_1, sorted_word_set_2))
    print(union(sorted_word_set_1, sorted_word_set_2))
    print(intersection(sorted_word_set_1, sorted_word_set_2))


if __name__ == "__main__":
    main()
