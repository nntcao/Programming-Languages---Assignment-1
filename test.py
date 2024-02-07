from setops import *

assert delimiter("", " ") == []
assert delimiter("      ", " ") == []
assert delimiter("   -   ", " ") == ["-"]
assert delimiter("a-s-b", "-") == ["a", "s", "b"]
assert delimiter("a s b", " ") == ["a", "s", "b"]
assert delimiter("   a   s       b     ", " ") == ["a", "s", "b"]
assert delimiter("a-s b", " ") == ["a-s", "b"]
assert delimiter("a-s b ", " ") == ["a-s", "b"]
assert delimiter(" a-s b ", " ") == ["a-s", "b"]
assert delimiter(" a", " ") == ["a"]
assert delimiter("a ", " ") == ["a"]
assert delimiter("   z   a   ", " ") == ["z", "a"]
assert delimiter("   z   a   ", " ") == ["z", "a"]
assert delimiter("   1232131   123658   ", " ") == ["1232131", "123658"]

assert remove_symbol("", "b") == ""
assert remove_symbol("aaaaa", "a") == ""
assert remove_symbol("aaaaab", "a") == "b"
assert remove_symbol("baaaaa", "a") == "b"
assert remove_symbol("aaabaa", "a") == "b"
assert remove_symbol("aaabaa", "b") == "aaaaa"
assert remove_symbol(" aaabaa", "b") == " aaaaa"

assert remove_symbols("./1/2.3,,,4", [".", "/", ","]) == "1234"
assert remove_symbols("./1/2.3,,,4", [".", ","]) == "/1/234"

assert to_lower("") == ""
assert to_lower("a") == "a"
assert to_lower("A") == "a"
assert to_lower("z") == "z"
assert to_lower("Z") == "z"
assert to_lower("g") == "g"
assert to_lower("G") == "g"
assert to_lower("ABC") == "abc"
assert to_lower("aBC") == "abc"
assert to_lower("abc./") == "abc./"
assert to_lower("Abc./") == "abc./"
assert to_lower("./Abc") == "./abc"
assert to_lower("123Abc") == "123abc"

assert linear_search([], "") == False
assert linear_search([], " ") == False
assert linear_search([1, 2, 3], 1) == True
assert linear_search([1, 2, 3], 2) == True
assert linear_search([1, 2, 3], 3) == True
assert linear_search([1, 2, 3], 4) == False
assert linear_search([""], " ") == False
assert linear_search([" "], " ") == True
assert linear_search(["a"], "b") == False
assert linear_search(["a"], "a") == True
assert linear_search(["b", "a"], "a") == True
assert linear_search(["a", "b"], "a") == True
assert linear_search(["a", "b", "c"], "d") == False
assert linear_search(["a", "b", "c"], "c") == True
assert linear_search(["\\", "SDKLFJ", "zxcklzxc"], "zxcklzxc") == True
assert linear_search(["\\", "SDKLFJ", "zxcklzxc"], "\\") == True

assert binary_search([], "") == False
assert binary_search([1, 2, 3], 0) == False
assert binary_search([1, 2, 3], 1) == True
assert binary_search([1, 2, 3], 2) == True
assert binary_search([1, 2, 3], 3) == True
assert binary_search([1, 2, 3], 4) == False
assert binary_search([1, 2, 3], 0) == False
assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == True
assert binary_search([1, 2, 3, 4, 5, 6, 7], 3) == True
assert binary_search([1, 2, 3, 4, 5, 6, 7], 5) == True
assert binary_search([1, 2, 3, 4, 5, 6, 7], 7) == True
assert binary_search([1, 2, 3, 4, 5, 6, 7], 0) == False
assert binary_search([1, 2, 3, 4, 5, 6, 7], 10) == False

assert replace_symbol("", "a", "c") == ""
assert replace_symbol("b", "a", "c") == "b"
assert replace_symbol("a", "a", "c") == "c"
assert replace_symbol("zza", "a", "c") == "zzc"
assert replace_symbol("azz", "a", "c") == "czz"
assert replace_symbol("zaz", "a", "c") == "zcz"
assert replace_symbol("  zaz", "a", "c") == "  zcz"
assert replace_symbol("zaz  ", "a", "c") == "zcz  "
assert replace_symbol(" zaz  ", "a", "c") == " zcz  "
assert replace_symbol("askjdhfkj\tsdfh", "\\", "\t") == "askjdhfkj\tsdfh"
assert replace_symbol("askjdhfkj\\sdfh", "\\", "\t") == "askjdhfkj\tsdfh"
assert replace_symbol("askjdhfkj\nsdfh", "\n", " ") == "askjdhfkj sdfh"

assert unique([]) == []
assert unique(["a"]) == ["a"]
assert unique(["a", "a"]) == ["a"]
assert unique(["a", "b"]) == ["a", "b"]
assert unique(["a", "a", "a"]) == ["a"]
assert unique(["a", "a", "b"]) == ["a", "b"]
assert unique(["a", "aaa", "b"]) == ["a", "aaa", "b"]
assert unique(["a", "b", "c", "c"]) == ["a", "b", "c"]
assert unique(["a", "a", "b", "c"]) == ["a", "b", "c"]
assert unique(["a", "a", "a", "b", "c"]) == ["a", "b", "c"]
assert unique(["a", "a", "b", "b", "c"]) == ["a", "b", "c"]
assert unique(["a", "b", "b", "b", "c"]) == ["a", "b", "c"]
assert unique(["111", "b", "c", "c"]) == ["111", "b", "c"]

assert sort([]) == []
assert sort(["a"]) == ["a"]
assert sort([0]) == [0]
assert sort([1]) == [1]
assert sort([1,2]) == [1,2]
assert sort([2,1]) == [1,2]
assert sort([1,2,5]) == [1,2,5]
assert sort([1,5,2]) == [1,2,5]
assert sort([2,1,5]) == [1,2,5]
assert sort([2,5,1]) == [1,2,5]
assert sort([5,2,1]) == [1,2,5]
assert sort([5,1,2]) == [1,2,5]
assert sort([5,1,2,4]) == [1,2,4,5]
assert sort([1,7,4,5,2]) == [1,2,4,5,7]
assert sort([7,1,5,2,4]) == [1,2,4,5,7]
assert sort([1,7,4,5,2,8]) == [1,2,4,5,7,8]
assert sort([8,7,4,5,2,1]) == [1,2,4,5,7,8]

assert difference([], []) == []
assert difference([1], []) == [1]
assert difference([], [1]) == [1]
assert difference([], [1, 2, 3]) == [1, 2, 3]
assert difference([1, 2, 3], []) == [1, 2, 3]
assert difference([1, 2, 3], [1, 2]) == [3]
assert difference([1, 2], [1, 2, 3]) == [3]
assert difference([1, 2, 3], [1, 2, 3]) == []
assert difference(["a", "b"], ["a", "b", "c"]) == ["c"]
assert difference(["b", "c"], ["a", "b", "c"]) == ["a"]
assert difference(["a", "c"], ["a", "b", "c"]) == ["b"]
assert difference(["a", "b", "c"], ["a", "b"]) == ["c"]
assert difference(["a", "b", "c"], ["b", "c"]) == ["a"]
assert difference(["a", "b", "c"], ["a", "c"]) == ["b"]
assert difference(["a", "b", "c"], ["a", "c", "d"]) == ["b", "d"]
assert difference(["bee", "bumble"], ["bee", "bumble", "buzz"]) == ["buzz"]
assert difference(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]) == ["bliss", "buzz"]
assert difference(["alpha", "beta"], ["alpha", "beta", "omega"]) == ["omega"]
assert difference(["beta", "omega"], ["alpha", "beta", "omega"]) == ["alpha"]

assert union([], []) == []
assert union([1], []) == [1]
assert union([], [1]) == [1]
assert union([], [1, 2, 3]) == [1, 2, 3]
assert union([1, 2, 3], []) == [1, 2, 3]
assert union([1, 2, 3], [1, 2]) == [1, 2, 3]
assert union([1, 2], [1, 2, 3]) == [1, 2, 3]
assert union([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
assert union(["a", "b"], ["a", "b", "c"]) == ["a", "b", "c"]
assert union(["b", "c"], ["a", "b", "c"]) == ["a", "b", "c"]
assert union(["a", "c"], ["a", "b", "c"]) == ["a", "b", "c"]
assert union(["a", "b", "c"], ["a", "b"]) == ["a", "b", "c"]
assert union(["a", "b", "c"], ["b", "c"]) == ["a", "b", "c"]
assert union(["a", "b", "c"], ["a", "c"]) == ["a", "b", "c"]
assert union(["bee", "bumble"], ["bee", "bumble", "buzz"]) == ["bee", "bumble", "buzz"]
assert union(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]) == ["bee", "bliss", "bumble", "buzz"]
assert union(["alpha", "beta"], ["alpha", "beta", "omega"]) == ["alpha", "beta", "omega"]
assert union(["beta", "omega"], ["alpha", "beta", "omega"]) == ["alpha", "beta", "omega"]

assert intersection([], []) == []
assert intersection([1], []) == []
assert intersection([], [1]) == []
assert intersection([], [1, 2, 3]) == []
assert intersection([1, 2, 3], []) == []
assert intersection([1, 2, 3], [1, 2]) == [1, 2]
assert intersection([1, 2], [1, 2, 3]) == [1, 2]
assert intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
assert intersection(["a", "b"], ["a", "b", "c"]) == ["a", "b"]
assert intersection(["b", "c"], ["a", "b", "c"]) == ["b", "c"]
assert intersection(["a", "c"], ["a", "b", "c"]) == ["a", "c"]
assert intersection(["a", "b", "c"], ["a", "b"]) == ["a", "b"]
assert intersection(["a", "b", "c"], ["b", "c"]) == ["b", "c"]
assert intersection(["a", "b", "c"], ["a", "c"]) == ["a", "c"]
assert intersection(["bee", "bumble"], ["bee", "bumble", "buzz"]) == ["bee", "bumble"]
assert intersection(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]) == ["bee", "bumble"]
assert intersection(["alpha", "beta"], ["alpha", "beta", "omega"]) == ["alpha", "beta"]
assert intersection(["beta", "omega"], ["alpha", "beta", "omega"]) == ["beta", "omega"]

