from setops import *
import unittest
import subprocess
import os

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

    def test_replace_symbols(self):
        self.assertEqual(replace_symbols(
            "abcdefg", ["a", "b"], "c"), "cccdefg")
        
    def test_is_numeric(self):
        self.assertEqual(is_numeric("a"), False)
        self.assertEqual(is_numeric("%"), False)
        self.assertEqual(is_numeric("!"), False)
        self.assertEqual(is_numeric(";"), False)
        self.assertEqual(is_numeric("1"), True)
        self.assertEqual(is_numeric("2"), True)
        self.assertEqual(is_numeric("3"), True)
        self.assertEqual(is_numeric("4"), True)
        self.assertEqual(is_numeric("5"), True)
        self.assertEqual(is_numeric("6"), True)
        self.assertEqual(is_numeric("7"), True)
        self.assertEqual(is_numeric("8"), True)
        self.assertEqual(is_numeric("9"), True)
        self.assertEqual(is_numeric("0"), True)
        self.assertEqual(is_numeric("10"), False)

    def test_is_alpha(self):
        self.assertEqual(is_alpha("a"), True)
        self.assertEqual(is_alpha("c"), True)
        self.assertEqual(is_alpha("z"), True)
        self.assertEqual(is_alpha("A"), True)
        self.assertEqual(is_alpha("C"), True)
        self.assertEqual(is_alpha("Z"), True)
        self.assertEqual(is_alpha("1"), False)
        self.assertEqual(is_alpha("7"), False)
        self.assertEqual(is_alpha("&"), False)

    def test_add_space_btwn_letter_number(self):
        self.assertEqual(add_space_between_letters_and_numbers("abc123"), "abc 123")
        self.assertEqual(add_space_between_letters_and_numbers("123abc"), "123 abc")
        self.assertEqual(add_space_between_letters_and_numbers("123456"), "123456")
        self.assertEqual(add_space_between_letters_and_numbers("abcdefg"), "abcdefg")
        self.assertEqual(add_space_between_letters_and_numbers("1A"), "1 A")
        self.assertEqual(add_space_between_letters_and_numbers("G1"), "G 1")
        self.assertEqual(add_space_between_letters_and_numbers("Z4"), "Z 4")

    def test_replace_periods(self):
        self.assertEqual(replace_periods("This is a sentence."), "This is a sentence ")
        self.assertEqual(replace_periods("This is a sentence.Testing!"), "This is a sentence Testing!")
        self.assertEqual(replace_periods("This is a 0.Testing!"), "This is a 0 Testing!")
        self.assertEqual(replace_periods("This is a 0.1 Testing!"), "This is a 0.1 Testing!")
        self.assertEqual(replace_periods("123.456.789"), "123.456 789")
        self.assertEqual(replace_periods("123.456.789.012"), "123.456 789.012")
        self.assertEqual(replace_periods("trying.this.out 123.456.789.012 123.456 123. and .123"), "trying this out 123.456 789.012 123.456 123  and  123")

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
        self.assertEqual(difference([], [1]), [])
        self.assertEqual(difference([], [1, 2, 3]), [])
        self.assertEqual(difference([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(difference([1, 2, 3], [1, 2]), [3])
        self.assertEqual(difference([1, 2], [1, 2, 3]), [])
        self.assertEqual(difference([1, 2, 3], [1, 2, 3]), [])
        self.assertEqual(difference(["a", "b"], ["a", "b", "c"]), [])
        self.assertEqual(difference(["b", "c"], ["a", "b", "c"]), [])
        self.assertEqual(difference(["a", "c"], ["a", "b", "c"]), [])
        self.assertEqual(difference(["a", "b", "c"], ["a", "b"]), ["c"])
        self.assertEqual(difference(["a", "b", "c"], ["b", "c"]), ["a"])
        self.assertEqual(difference(["a", "b", "c"], ["a", "c"]), ["b"])
        self.assertEqual(difference(["a", "b", "c"], ["a", "c", "d"]), ["b"])
        self.assertEqual(difference(["bee", "bumble"], ["bee", "bumble", "buzz"]), [])
        self.assertEqual(difference(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]), ["bliss"])
        self.assertEqual(difference(["alpha", "beta", "omega"], ["alpha", "beta"]), ["omega"])
        self.assertEqual(difference(["alpha", "beta", "omega"], ["beta", "omega"]), ["alpha"])

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


class TestSetOps(unittest.TestCase):

    def test_setops(self):
        def generate_py_setops_cmd(set1, set2, operation):
            return f"python setops.py \"set1={set1};set2={set2};operation={operation}\""

        def generate_py3_setops_cmd(set1, set2, operation):
            return f"python3 setops.py \"set1={set1};set2={set2};operation={operation}\""

        def read_output_txt():
            with open("result.txt", "r") as o:
                return o.read()

        def read_txt(filepath):
            with open(filepath, "r") as f:
                return f.read()

        def run_test(set1, set2, operation, answer):
            if sys.platform == "win32":
                subprocess.run(generate_py_setops_cmd(os.path.abspath(set1), os.path.abspath(set2), operation), shell=True)
            else:
                subprocess.run(generate_py3_setops_cmd(os.path.abspath(set1), os.path.abspath(set2), operation), shell=True)

            self.assertEqual(read_output_txt(), read_txt(os.path.abspath(answer)))

        run_test("./test/a.txt", "./test/b.txt",
                 "intersection", "./test/a_b_intersection.txt")
        run_test("./test/a.txt", "./test/b.txt",
                 "union", "./test/a_b_union.txt")
        run_test("./test/a.txt", "./test/b.txt",
                 "difference", "./test/a_b_difference.txt")

        run_test("./test/c.txt", "./test/d.txt",
                 "intersection", "./test/c_d_intersection.txt")
        run_test("./test/c.txt", "./test/d.txt",
                 "union", "./test/c_d_union.txt")
        run_test("./test/c.txt", "./test/d.txt",
                 "difference", "./test/c_d_difference.txt")

        run_test("./test/e.txt", "./test/f.txt",
                 "intersection", "./test/e_f_intersection.txt")
        run_test("./test/e.txt", "./test/f.txt",
                 "union", "./test/e_f_union.txt")

        run_test("./test/g.txt", "./test/h.txt",
                 "intersection", "./test/g_h_intersection.txt")
        run_test("./test/g.txt", "./test/h.txt",
                 "union", "./test/g_h_union.txt")

        run_test("./test/a1.txt", "./test/b1.txt",
                 "intersection", "./test/result1.txt")
        run_test("./test/a2.txt", "./test/b2.txt",
                 "difference", "./test/result2.txt")
        run_test("./test/a3.txt", "./test/b3.txt",
                 "union", "./test/result3.txt")
        run_test("./test/a4.txt", "./test/b4.txt",
                 "intersection", "./test/result4.txt")

        run_test("./test/testcase1.txt", "./test/testcase2.txt",
                 "intersection", "./test/testcase1_testcase2_intersection.txt")
        run_test("./test/testcase1.txt", "./test/testcase2.txt",
                 "difference", "./test/testcase1_testcase2_difference.txt")
        run_test("./test/testcase1.txt", "./test/testcase2.txt",
                 "union", "./test/testcase1_testcase2_union.txt")


if __name__ == '__main__':
    unittest.main()
