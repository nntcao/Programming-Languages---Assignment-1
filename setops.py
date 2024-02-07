
def delimiter_helper_get_word(string, symbol):
    if not string or string[0] == symbol:
        return ""
    return string[0] + delimiter_helper_get_word(string[1:], symbol)

def delimiter_helper_next(string, symbol):
    if not string:
        return []
    if string[0] == symbol and string[1] != symbol:
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

# returns list l with only unique values
def unique(l):
    if not l:
        return []
    if exists(l[1:], l[0]):
        return unique(l[1:])
    return [l[0]] + unique(l[1:])

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

if __name__ == "__main__":
    main()
