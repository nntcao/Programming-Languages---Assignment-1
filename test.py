from setops import *
import unittest


class TestSortMethods(unittest.TestCase):

    def test_is_sorted_asc(self):
        self.assertEqual(is_sorted_asc([]), True)
        self.assertEqual(is_sorted_asc([1]), True)
        self.assertEqual(is_sorted_asc([1, 2, 3, 4]), True)
        self.assertEqual(is_sorted_asc([1, 3, 3, 4]), True)
        self.assertEqual(is_sorted_asc([6, 3, 3, 4]), False)
        self.assertEqual(is_sorted_asc(["a", "b", "c"]), True)
        self.assertEqual(is_sorted_asc(["a", "b", "a"]), False)

    def test_sort(self):
        self.assertEqual(sort([]), [])
        self.assertEqual(sort(["a"]), ["a"])
        self.assertEqual(sort([0]), [0])
        self.assertEqual(sort([1]), [1])
        self.assertEqual(sort([1, 2]), [1, 2])
        self.assertEqual(sort([2, 1]), [1, 2])
        self.assertEqual(sort([1, 2, 5]), [1, 2, 5])
        self.assertEqual(sort([1, 5, 2]), [1, 2, 5])
        self.assertEqual(sort([2, 1, 5]), [1, 2, 5])
        self.assertEqual(sort([2, 5, 1]), [1, 2, 5])
        self.assertEqual(sort([5, 2, 1]), [1, 2, 5])
        self.assertEqual(sort([5, 1, 2]), [1, 2, 5])
        self.assertEqual(sort([5, 1, 2, 4]), [1, 2, 4, 5])
        self.assertEqual(sort([1, 7, 4, 5, 2]), [1, 2, 4, 5, 7])
        self.assertEqual(sort([7, 1, 5, 2, 4]), [1, 2, 4, 5, 7])
        self.assertEqual(sort([1, 7, 4, 5, 2, 8]), [1, 2, 4, 5, 7, 8])
        self.assertEqual(sort([8, 7, 4, 5, 2, 1]), [1, 2, 4, 5, 7, 8])


class TestStringMethods(unittest.TestCase):

    def test_delimiter(self):
        self.assertEqual(delimiter("", " "), [])
        self.assertEqual(delimiter("      ", " "), [])
        self.assertEqual(delimiter("   -   ", " "), ["-"])
        self.assertEqual(delimiter("a-s-b", "-"), ["a", "s", "b"])
        self.assertEqual(delimiter("a s b", " "), ["a", "s", "b"])
        self.assertEqual(
            delimiter("   a   s       b     ", " "), ["a", "s", "b"])
        self.assertEqual(delimiter("a-s b", " "), ["a-s", "b"])
        self.assertEqual(delimiter("a-s b ", " "), ["a-s", "b"])
        self.assertEqual(delimiter(" a-s b ", " "), ["a-s", "b"])
        self.assertEqual(delimiter(" a", " "), ["a"])
        self.assertEqual(delimiter("a ", " "), ["a"])
        self.assertEqual(delimiter("   z   a   ", " "), ["z", "a"])
        self.assertEqual(delimiter("   z   a   ", " "), ["z", "a"])
        self.assertEqual(delimiter("   1232131   123658   ", " "), [
                         "1232131", "123658"])

    def test_remove_symbol(self):
        self.assertEqual(remove_symbol("", "b"), "")
        self.assertEqual(remove_symbol("aaaaa", "a"), "")
        self.assertEqual(remove_symbol("aaaaab", "a"), "b")
        self.assertEqual(remove_symbol("baaaaa", "a"), "b")
        self.assertEqual(remove_symbol("aaabaa", "a"), "b")
        self.assertEqual(remove_symbol("aaabaa", "b"), "aaaaa")
        self.assertEqual(remove_symbol(" aaabaa", "b"), " aaaaa")
        self.assertEqual(remove_symbols(
            "./1/2.3,,,4", [".", "/", ","]), "1234")
        self.assertEqual(remove_symbols("./1/2.3,,,4", [".", ","]), "/1/234")

    def test_to_lower(self):
        self.assertEqual(to_lower(""), "")
        self.assertEqual(to_lower("a"), "a")
        self.assertEqual(to_lower("A"), "a")
        self.assertEqual(to_lower("z"), "z")
        self.assertEqual(to_lower("Z"), "z")
        self.assertEqual(to_lower("g"), "g")
        self.assertEqual(to_lower("G"), "g")
        self.assertEqual(to_lower("ABC"), "abc")
        self.assertEqual(to_lower("aBC"), "abc")
        self.assertEqual(to_lower("abc./"), "abc./")
        self.assertEqual(to_lower("Abc./"), "abc./")
        self.assertEqual(to_lower("./Abc"), "./abc")
        self.assertEqual(to_lower("123Abc"), "123abc")

    def test_replace_symbol(self):
        self.assertEqual(replace_symbol("", "a", "c"), "")
        self.assertEqual(replace_symbol("b", "a", "c"), "b")
        self.assertEqual(replace_symbol("a", "a", "c"), "c")
        self.assertEqual(replace_symbol("zza", "a", "c"), "zzc")
        self.assertEqual(replace_symbol("azz", "a", "c"), "czz")
        self.assertEqual(replace_symbol("zaz", "a", "c"), "zcz")
        self.assertEqual(replace_symbol("  zaz", "a", "c"), "  zcz")
        self.assertEqual(replace_symbol("zaz  ", "a", "c"), "zcz  ")
        self.assertEqual(replace_symbol(" zaz  ", "a", "c"), " zcz  ")
        self.assertEqual(replace_symbol(
            "askjdhfkj\tsdfh", "\\", "\t"), "askjdhfkj\tsdfh")
        self.assertEqual(replace_symbol(
            "askjdhfkj\\sdfh", "\\", "\t"), "askjdhfkj\tsdfh")
        self.assertEqual(replace_symbol(
            "askjdhfkj\nsdfh", "\n", " "), "askjdhfkj sdfh")


class TestSearchMethods(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([], ""), False)
        self.assertEqual(linear_search([], " "), False)
        self.assertEqual(linear_search([1, 2, 3], 1), True)
        self.assertEqual(linear_search([1, 2, 3], 2), True)
        self.assertEqual(linear_search([1, 2, 3], 3), True)
        self.assertEqual(linear_search([1, 2, 3], 4), False)
        self.assertEqual(linear_search([""], " "), False)
        self.assertEqual(linear_search([" "], " "), True)
        self.assertEqual(linear_search(["a"], "b"), False)
        self.assertEqual(linear_search(["a"], "a"), True)
        self.assertEqual(linear_search(["b", "a"], "a"), True)
        self.assertEqual(linear_search(["a", "b"], "a"), True)
        self.assertEqual(linear_search(["a", "b", "c"], "d"), False)
        self.assertEqual(linear_search(["a", "b", "c"], "c"), True)
        self.assertEqual(linear_search(
            ["\\", "SDKLFJ", "zxcklzxc"], "zxcklzxc"), True)
        self.assertEqual(linear_search(
            ["\\", "SDKLFJ", "zxcklzxc"], "\\"), True)

    def test_binary_search(self):
        self.assertEqual(binary_search([], ""), False)
        self.assertEqual(binary_search([1, 2, 3], 0), False)
        self.assertEqual(binary_search([1, 2, 3], 1), True)
        self.assertEqual(binary_search([1, 2, 3], 2), True)
        self.assertEqual(binary_search([1, 2, 3], 3), True)
        self.assertEqual(binary_search([1, 2, 3], 4), False)
        self.assertEqual(binary_search([1, 2, 3], 0), False)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 1), True)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 3), True)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 5), True)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 7), True)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 0), False)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 10), False)


class TestSetMethods(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(unique([]), [])
        self.assertEqual(unique(["a"]), ["a"])
        self.assertEqual(unique(["a", "a"]), ["a"])
        self.assertEqual(unique(["a", "b"]), ["a", "b"])
        self.assertEqual(unique(["a", "a", "a"]), ["a"])
        self.assertEqual(unique(["a", "a", "b"]), ["a", "b"])
        self.assertEqual(unique(["a", "aaa", "b"]), ["a", "aaa", "b"])
        self.assertEqual(unique(["a", "b", "c", "c"]), ["a", "b", "c"])
        self.assertEqual(unique(["a", "a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(unique(["a", "a", "a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(unique(["a", "a", "b", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(unique(["a", "b", "b", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(unique(["111", "b", "c", "c"]), ["111", "b", "c"])

    def test_difference(self):
        self.assertEqual(difference([], []), [])
        self.assertEqual(difference([1], []), [1])
        self.assertEqual(difference([], [1]), [1])
        self.assertEqual(difference([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(difference([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(difference([1, 2, 3], [1, 2]), [3])
        self.assertEqual(difference([1, 2], [1, 2, 3]), [3])
        self.assertEqual(difference([1, 2, 3], [1, 2, 3]), [])
        self.assertEqual(difference(["a", "b"], ["a", "b", "c"]), ["c"])
        self.assertEqual(difference(["b", "c"], ["a", "b", "c"]), ["a"])
        self.assertEqual(difference(["a", "c"], ["a", "b", "c"]), ["b"])
        self.assertEqual(difference(["a", "b", "c"], ["a", "b"]), ["c"])
        self.assertEqual(difference(["a", "b", "c"], ["b", "c"]), ["a"])
        self.assertEqual(difference(["a", "b", "c"], ["a", "c"]), ["b"])
        self.assertEqual(difference(["a", "b", "c"], [
                         "a", "c", "d"]), ["b", "d"])
        self.assertEqual(difference(["bee", "bumble"], [
                         "bee", "bumble", "buzz"]), ["buzz"])
        self.assertEqual(difference(["bee", "bliss", "bumble"], [
                         "bee", "bumble", "buzz"]), ["bliss", "buzz"])
        self.assertEqual(difference(["alpha", "beta"], [
                         "alpha", "beta", "omega"]), ["omega"])
        self.assertEqual(difference(["beta", "omega"], [
                         "alpha", "beta", "omega"]), ["alpha"])

    def test_union(self):
        self.assertEqual(union([], []), [])
        self.assertEqual(union([1], []), [1])
        self.assertEqual(union([], [1]), [1])
        self.assertEqual(union([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(union([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(union([1, 2, 3], [1, 2]), [1, 2, 3])
        self.assertEqual(union([1, 2], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(union([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(union(["a", "b"], ["a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(union(["b", "c"], ["a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(union(["a", "c"], ["a", "b", "c"]), ["a", "b", "c"])
        self.assertEqual(union(["a", "b", "c"], ["a", "b"]), ["a", "b", "c"])
        self.assertEqual(union(["a", "b", "c"], ["b", "c"]), ["a", "b", "c"])
        self.assertEqual(union(["a", "b", "c"], ["a", "c"]), ["a", "b", "c"])
        self.assertEqual(union(["bee", "bumble"], ["bee", "bumble", "buzz"]), [
                         "bee", "bumble", "buzz"])
        self.assertEqual(union(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]), [
                         "bee", "bliss", "bumble", "buzz"])
        self.assertEqual(union(["alpha", "beta"], ["alpha", "beta", "omega"]), [
                         "alpha", "beta", "omega"])
        self.assertEqual(union(["beta", "omega"], ["alpha", "beta", "omega"]), [
                         "alpha", "beta", "omega"])

    def test_intersection(self):
        self.assertEqual(intersection([], []), [])
        self.assertEqual(intersection([1], []), [])
        self.assertEqual(intersection([], [1]), [])
        self.assertEqual(intersection([], [1, 2, 3]), [])
        self.assertEqual(intersection([1, 2, 3], []), [])
        self.assertEqual(intersection([1, 2, 3], [1, 2]), [1, 2])
        self.assertEqual(intersection([1, 2], [1, 2, 3]), [1, 2])
        self.assertEqual(intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(intersection(["a", "b"], ["a", "b", "c"]), ["a", "b"])
        self.assertEqual(intersection(["b", "c"], ["a", "b", "c"]), ["b", "c"])
        self.assertEqual(intersection(["a", "c"], ["a", "b", "c"]), ["a", "c"])
        self.assertEqual(intersection(["a", "b", "c"], ["a", "b"]), ["a", "b"])
        self.assertEqual(intersection(["a", "b", "c"], ["b", "c"]), ["b", "c"])
        self.assertEqual(intersection(["a", "b", "c"], ["a", "c"]), ["a", "c"])
        self.assertEqual(intersection(["bee", "bumble"], [
                         "bee", "bumble", "buzz"]), ["bee", "bumble"])
        self.assertEqual(intersection(["bee", "bliss", "bumble"], [
                         "bee", "bumble", "buzz"]), ["bee", "bumble"])
        self.assertEqual(intersection(["alpha", "beta"], [
                         "alpha", "beta", "omega"]), ["alpha", "beta"])
        self.assertEqual(intersection(["beta", "omega"], [
                         "alpha", "beta", "omega"]), ["beta", "omega"])


if __name__ == '__main__':
    unittest.main()
