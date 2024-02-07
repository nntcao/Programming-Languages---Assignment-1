
def _delimiter_helper_get_word(string, symbol):
    # "Gets" the word until a delimiter is reached
    if not string or string[0] == symbol:
        return ""
    return string[0] + _delimiter_helper_get_word(string[1:], symbol)


def _delimiter_helper_next(string, symbol):
    # Since delimiting requires two different operations: to "get" the word, and find where the next word starts,
    #   two helper functions are needed
    if not string:
        return []
    # By checking if the current symbol is the delimiter AND the next is not, duplicate delimiters are ignored
    if len(string) > 1 and string[0] == symbol and string[1] != symbol:
        return [_delimiter_helper_get_word(string[1:], symbol)] + _delimiter_helper_next(string[1:], symbol)
    return _delimiter_helper_next(string[1:], symbol)


def delimiter(string: str, symbol: str) -> list[str]:
    """Splits a string by delimiter symbol into a list of strings
    
    Args:
        string (str): the string to split
        symbol (str): the single character symbol to split by

    Returns:
        list[str]: a list of strings broken up by the delimiter function.
    """
    if not string:
        return []
    return _delimiter_helper_next(symbol + string, symbol)


def remove_symbol(string, symbol):
    """Removes all occurances of a symbol from a string

    Args:
        string (str): the string to remove symbols from
        symbol (str): the single char symbol to remove

    Returns:
        str: the input string with all symbols removed
    """
    if not string:
        return ""
    if string[0] == symbol:
        return remove_symbol(string[1:], symbol)
    return string[0] + remove_symbol(string[1:], symbol)


def remove_symbols(string: str, symbols: list[str]):
    """Removes all occurances symbols from a string

    Args:
        string (str): the string to remove symbols from
        symbols (list[str]): list of symbols to remove

    Returns:
        str: the input string with all symbols removed
    """
    if not symbols:
        return string
    return remove_symbols(remove_symbol(string, symbols[0]), symbols[1:])


def to_lower(string: str):
    """Changes all uppercase letters to lowercase letters

    Args:
        string (str): the string to change to lowercase

    Returns:
        str: lowercase version of string
    """
    if not string:
        return ""
    if 65 <= ord(string[0]) and ord(string[0]) <= 90:
        return chr(ord(string[0]) + 32) + to_lower(string[1:])
    return string[0] + to_lower(string[1:])


def linear_search(l: list[any], element: any):
    """Completes a linear search for the element

    Args:
        l (list[any]): a list to search
        element (any): the element to search for

    Returns:
        bool: True if the element is found, False otherwise
    """
    if not l:
        return False
    if l[0] == element:
        return True
    return linear_search(l[1:], element)


def binary_search(l: list[any], element: any):
    """Completes a binary search for the element

    Args:
        l (list[any]): a sorted list to search
        element (any): the element to search for

    Returns:
        bool: True if the element is found, False otherwise
    """
    if not l:
        return False
    if l[len(l) // 2] == element:
        return True
    if l[len(l) // 2] < element:
        return binary_search(l[len(l) // 2 + 1:], element)
    return binary_search(l[:len(l) // 2], element)


def replace_symbol(string: str, old_symbol: str, new_symbol: str):
    """Replaces all old symbols with new symbols in a string

    Args:
        string (str): the string to replace symbols in
        old_symbol (str): the old symbol to be replaced
        new_symbol (str): the new symbol to replace

    Returns:
        str: the string with the new symbols replacing the old symbols
    """
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


def unique(sorted_list: list[any]):
    """Removes all duplicate values from the list

    Returns the list with only unique values. The algorithm operates under
    the assumption the list is sorted. It executes in time complexity of
    O(n).

    Args:
        sorted_list (list[any]): a sorted list

    Returns:
        list[any]: the list without any duplicate values
    """
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


def sort(l: list[any]):
    """Sorts a list in ascending order

    This sorting operation is implemented using merge sort. The time complexity
    is O(n * log(n)).

    Args:
        l (list[any]): the list to be sorted

    Returns:
        list[any]: the sorted list in ascending order
    """
    return _merge_sort(l)


def _difference_helper(sorted_set_1, sorted_set_2):
    # since they are both sorted, we can exploit that and search for an "equal" word in O(n+m) time
    if not sorted_set_1:
        return sorted_set_2
    if not sorted_set_2:
        return sorted_set_1
    if sorted_set_1[0] == sorted_set_2[0]:
        return _difference_helper(sorted_set_1[1:], sorted_set_2[1:])
    if sorted_set_1[0] < sorted_set_2[0]:
        return [sorted_set_1[0]] + _difference_helper(sorted_set_1[1:], sorted_set_2)
    return [sorted_set_2[0]] + _difference_helper(sorted_set_1, sorted_set_2[1:])


def difference(sorted_set_1: list[any], sorted_set_2: list[any]):
    """Finds the set difference of the two input sets

    This operation assumes two properties of the inputs: a sorted list, and a set,
    which implies all elements are unique.

    Args:
        sorted_set_1 (list[any]): the first sorted set
        sorted_set_2 (list[any]): the second sorted set

    Returns:
        list[any]: a sorted set containing only the differences
    """
    return sort(_difference_helper(sorted_set_1, sorted_set_2))


def union(sorted_set_1: list[any], sorted_set_2: list[any]):
    """Finds the set union of the two input sets

    This operation assumes two properties of the inputs: a sorted list, and a set,
    which implies all elements are unique.

    Args:
        sorted_set_1 (list[any]): the first sorted set
        sorted_set_2 (list[any]): the second sorted set

    Returns:
        list[any]: a sorted set union of the two input sets
    """
    return unique(sort(sorted_set_1 + sorted_set_2))


def _intersection_helper(sorted_set_1, sorted_set_2):
    # since they are both sorted, we can exploit that and search for an "equal" word in O(n+m) time
    if not sorted_set_1 or not sorted_set_2:
        return []
    if sorted_set_1[0] == sorted_set_2[0]:
        return [sorted_set_1[0]] + _intersection_helper(sorted_set_1[1:], sorted_set_2[1:])
    if sorted_set_1[0] < sorted_set_2[0]:
        return _intersection_helper(sorted_set_1[1:], sorted_set_2)
    return _intersection_helper(sorted_set_1, sorted_set_2[1:])


def intersection(sorted_set_1: list[any], sorted_set_2: list[any]):
    """Finds the set intersection of the two input sets

    This operation assumes two properties of the inputs: a sorted list, and a set,
    which implies all elements are unique.

    Args:
        sorted_set_1 (list[any]): the first sorted set
        sorted_set_2 (list[any]): the second sorted set

    Returns:
        list[any]: a sorted set intersection of the two input sets
    """
    return sort(_intersection_helper(sorted_set_1, sorted_set_2))


def string_to_sorted_word_set(string: str):
    """Organizes a string into a sorted word set

    Takes a string and cleans it of all punctuation. Then, it replaces
    all \\n, \\r, and \\t characters with a space character. This is so
    all words are captured and aren't accidently combined.

    After cleaning, the delimiter (with symbol " ") is executed and a list 
    of words is created. The list of words are all transformed to lowercase 
    using the map function.

    Finally, the list of words are sorted and duplicates are removed, which
    creates the sorted word set.

    Args:
        string (str): the string to make a word set of

    Returns:
        list[str]: a sorted set of words made up of the words in the string
    """
    # expanded for readability---lovely scheme-esque formatting :)
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
    sorted_word_set_1 = string_to_sorted_word_set(text1)
    sorted_word_set_2 = string_to_sorted_word_set(text2)
    print(sorted_word_set_1)
    print(sorted_word_set_2)

    print(difference(sorted_word_set_1, sorted_word_set_2))
    print(union(sorted_word_set_1, sorted_word_set_2))
    print(intersection(sorted_word_set_1, sorted_word_set_2))


if __name__ == "__main__":
    main()
