import sys


def is_sorted_asc(sorted_list: list[any]):
    """Determines if list is sorted ascending

    Args:
        sorted_list (list[any]): the list to evaluate

    Returns:
        bool: True if sorted ascending, False otherwise
    """
    if len(sorted_list) <= 1:
        return True
    if sorted_list[0] > sorted_list[1]:
        return False
    return is_sorted_asc(sorted_list[1:])


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


def _binary_search_helper(sorted_list, element):
    if not sorted_list:
        return False
    if sorted_list[len(sorted_list) // 2] == element:
        return True
    if sorted_list[len(sorted_list) // 2] < element:
        return _binary_search_helper(sorted_list[len(sorted_list) // 2 + 1:], element)
    return _binary_search_helper(sorted_list[:len(sorted_list) // 2], element)


def binary_search(sorted_list: list[any], element: any):
    """Completes a binary search for the element

    Args:
        l (list[any]): a sorted list to search
        element (any): the element to search for

    Returns:
        bool: True if the element is found, False otherwise
    """
    if not is_sorted_asc(sorted_list):
        raise ValueError("list must be sorted to call binary search function")
    return _binary_search_helper(sorted_list, element)


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


def replace_symbols(string: str, old_symbols: list[str], new_symbol: str):
    if not string:
        return ""
    if not old_symbols:
        return string
    return replace_symbols(replace_symbol(string, old_symbols[0], new_symbol), old_symbols[1:], new_symbol)

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
    if not is_sorted_asc(sorted_list):
        raise ValueError("list must be sorted to call unique function")
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
    if not is_sorted_asc(sorted_set_1) or not is_sorted_asc(sorted_set_2):
        raise ValueError("list must be sorted to call set difference function")
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
    if not is_sorted_asc(sorted_set_1) or not is_sorted_asc(sorted_set_2):
        raise ValueError("list must be sorted to call set union function")
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
    if not is_sorted_asc(sorted_set_1) or not is_sorted_asc(sorted_set_2):
        raise ValueError(
            "list must be sorted to call set intersection function")
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


def get_cli_input() -> list[str]:
    if len(sys.argv) != 2:
        print(
            "Usage: setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        exit(1)

    text_cli_args = sys.argv[1]
    var_list = delimiter(text_cli_args, ";")

    if len(var_list) != 3:
        print(
            "Usage: setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        exit(1)

    filepath_1 = delimiter(var_list[0], "=")
    filepath_2 = delimiter(var_list[1], "=")
    operation = delimiter(var_list[2], "=")

    if len(filepath_1) != 2 or len(filepath_2) != 2 or len(operation) != 2:
        print(
            "Usage: setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        exit(1)

    if not (operation[1] == "difference" or operation[1] == "union" or operation[1] == "intersection"):
        print(
            "Usage: setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        exit(1)

    return [filepath_1[1], filepath_2[1], operation[1]]


def write_output_helper(output_file, results: list[str]):
    if not results:
        return []
    output_file.write("\n" + results[0])
    return write_output_helper(output_file, results[1:])


def write_output(results: list[str]) -> list[str]:
    with open("output.txt", "w") as output_file:
        if not results:
            output_file.write("empty set")
        else:
            output_file.write(results[0])
            write_output_helper(output_file, results[1:])


def main():

    filepath_1, filepath_2, operation = get_cli_input()

    try:
        file1 = open(filepath_1)
    except OSError:
        print("Could not open file: " + filepath_1)
        sys.exit(1)

    try:
        file2 = open(filepath_2)
    except OSError:
        print("Could not open file: " + filepath_2)
        sys.exit(1)

    with file1, file2:
        text1 = file1.read()
        text2 = file2.read()

    if operation == "difference":
        write_output(difference(string_to_sorted_word_set(
            text1), string_to_sorted_word_set(text2)))
    if operation == "union":
        write_output(union(string_to_sorted_word_set(
            text1), string_to_sorted_word_set(text2)))
    if operation == "intersection":
        write_output(intersection(string_to_sorted_word_set(
            text1), string_to_sorted_word_set(text2)))


if __name__ == "__main__":
    main()
