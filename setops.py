
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

def main():
    print(delimiter("sudden attack", " "))
    print(delimiter("      sudden attack", " "))
    print(delimiter(" sudden          attack", " "))
    print(delimiter(" sudden          attack parrot chopper test", " "))
    print(remove_symbol("Dog jump over moon. And shot, at sun. And become world.", "."))
    print(to_lower("aaAAAAaa!.AAaaAAA"))

    #file1 = open(set1)
    #set1 = file1.read()
    #print(set1)

    #file2 = open(set2)
    #set2 = file2.read()
    #print(set2)
    #file1.close()
    #file2.close()

if __name__ == "__main__":
    main()
