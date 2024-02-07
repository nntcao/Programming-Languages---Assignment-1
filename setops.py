
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
    print(delimiter("sudden attack", " "))
    print(delimiter("      sudden attack", " "))
    print(delimiter(" sudden          attack", " "))
    print(delimiter(" sudden          attack parrot chopper test", " "))
    print(remove_symbol("Dog jump over moon. And shot, at sun. And become world.", "."))
    print(to_lower("aaAAAAaa!.AAaaAAA"))
    print(unique([1,1,1,2,3,4,5,6,7,8,8,123]))


if __name__ == "__main__":
    main()