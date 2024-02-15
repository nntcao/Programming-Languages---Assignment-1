const fs = require('fs');
const assert = require('assert')
const childProcess = require('child_process');

const {
    isSortedAsc,
    sort,
    delimiter,
    removeSymbol,
    removeSymbols,
    toLower,
    replaceSymbol,
    replaceSymbols,
    isNumeric,
    isAlpha,
    addSpaceBetweenLettersAndNumbers,
    replacePeriods,
    linearSearch,
    binarySearch,
    unique,
    difference,
    union,
    intersection,
} = require('./setops.js');  // Replace './setops' with the actual path to your setops module
  
function testisSortedAsc() {
    assert.deepStrictEqual(isSortedAsc([]), true)
    assert.deepStrictEqual(isSortedAsc([1]), true)
    assert.deepStrictEqual(isSortedAsc([1, 2, 3, 4]), true)
    assert.deepStrictEqual(isSortedAsc([1, 3, 3, 4]), true)
    assert.deepStrictEqual(isSortedAsc([6, 3, 3, 4]), false)
    assert.deepStrictEqual(isSortedAsc(["a", "b", "c"]), true)
    assert.deepStrictEqual(isSortedAsc(["a", "b", "a"]), false)
}

function testsort() {
    assert.deepStrictEqual(sort([]), [])
    assert.deepStrictEqual(sort(["a"]), ["a"])
    assert.deepStrictEqual(sort([0]), [0])
    assert.deepStrictEqual(sort([1]), [1])
    assert.deepStrictEqual(sort([1, 2]), [1, 2])
    assert.deepStrictEqual(sort([2, 1]), [1, 2])
    assert.deepStrictEqual(sort([1, 2, 5]), [1, 2, 5])
    assert.deepStrictEqual(sort([1, 5, 2]), [1, 2, 5])
    assert.deepStrictEqual(sort([2, 1, 5]), [1, 2, 5])
    assert.deepStrictEqual(sort([2, 5, 1]), [1, 2, 5])
    assert.deepStrictEqual(sort([5, 2, 1]), [1, 2, 5])
    assert.deepStrictEqual(sort([5, 1, 2]), [1, 2, 5])
    assert.deepStrictEqual(sort([5, 1, 2, 4]), [1, 2, 4, 5])
    assert.deepStrictEqual(sort([1, 7, 4, 5, 2]), [1, 2, 4, 5, 7])
    assert.deepStrictEqual(sort([7, 1, 5, 2, 4]), [1, 2, 4, 5, 7])
    assert.deepStrictEqual(sort([1, 7, 4, 5, 2, 8]), [1, 2, 4, 5, 7, 8])
    assert.deepStrictEqual(sort([8, 7, 4, 5, 2, 1]), [1, 2, 4, 5, 7, 8])
}


function testdelimiter() {
    assert.deepStrictEqual(delimiter("", " "), [])
    assert.deepStrictEqual(delimiter("      ", " "), [])
    assert.deepStrictEqual(delimiter("   -   ", " "), ["-"])
    assert.deepStrictEqual(delimiter("a-s-b", "-"), ["a", "s", "b"])
    assert.deepStrictEqual(delimiter("a s b", " "), ["a", "s", "b"])
    assert.deepStrictEqual(delimiter("   a   s       b     ", " "), ["a", "s", "b"])
    assert.deepStrictEqual(delimiter("a-s b", " "), ["a-s", "b"])
    assert.deepStrictEqual(delimiter("a-s b ", " "), ["a-s", "b"])
    assert.deepStrictEqual(delimiter(" a-s b ", " "), ["a-s", "b"])
    assert.deepStrictEqual(delimiter(" a", " "), ["a"])
    assert.deepStrictEqual(delimiter("a ", " "), ["a"])
    assert.deepStrictEqual(delimiter("   z   a   ", " "), ["z", "a"])
    assert.deepStrictEqual(delimiter("   z   a   ", " "), ["z", "a"])
    assert.deepStrictEqual(delimiter("   1232131   123658   ", " "), ["1232131", "123658"])
}

function testremoveSymbol() {
    assert.deepStrictEqual(removeSymbol("", "b"), "")
    assert.deepStrictEqual(removeSymbol("aaaaa", "a"), "")
    assert.deepStrictEqual(removeSymbol("aaaaab", "a"), "b")
    assert.deepStrictEqual(removeSymbol("baaaaa", "a"), "b")
    assert.deepStrictEqual(removeSymbol("aaabaa", "a"), "b")
    assert.deepStrictEqual(removeSymbol("aaabaa", "b"), "aaaaa")
    assert.deepStrictEqual(removeSymbol(" aaabaa", "b"), " aaaaa")
    assert.deepStrictEqual(removeSymbols("./1/2.3,,,4", [".", "/", ","]), "1234")
    assert.deepStrictEqual(removeSymbols("./1/2.3,,,4", [".", ","]), "/1/234")
}

function testtoLower() {
    assert.deepStrictEqual(toLower(""), "")
    assert.deepStrictEqual(toLower("a"), "a")
    assert.deepStrictEqual(toLower("A"), "a")
    assert.deepStrictEqual(toLower("z"), "z")
    assert.deepStrictEqual(toLower("Z"), "z")
    assert.deepStrictEqual(toLower("g"), "g")
    assert.deepStrictEqual(toLower("G"), "g")
    assert.deepStrictEqual(toLower("ABC"), "abc")
    assert.deepStrictEqual(toLower("aBC"), "abc")
    assert.deepStrictEqual(toLower("abc./"), "abc./")
    assert.deepStrictEqual(toLower("Abc./"), "abc./")
    assert.deepStrictEqual(toLower("./Abc"), "./abc")
    assert.deepStrictEqual(toLower("123Abc"), "123abc")
}

function testreplaceSymbol() {
    assert.deepStrictEqual(replaceSymbol("", "a", "c"), "")
    assert.deepStrictEqual(replaceSymbol("b", "a", "c"), "b")
    assert.deepStrictEqual(replaceSymbol("a", "a", "c"), "c")
    assert.deepStrictEqual(replaceSymbol("zza", "a", "c"), "zzc")
    assert.deepStrictEqual(replaceSymbol("azz", "a", "c"), "czz")
    assert.deepStrictEqual(replaceSymbol("zaz", "a", "c"), "zcz")
    assert.deepStrictEqual(replaceSymbol("  zaz", "a", "c"), "  zcz")
    assert.deepStrictEqual(replaceSymbol("zaz  ", "a", "c"), "zcz  ")
    assert.deepStrictEqual(replaceSymbol(" zaz  ", "a", "c"), " zcz  ")
    assert.deepStrictEqual(replaceSymbol("askjdhfkj\tsdfh", "\\", "\t"), "askjdhfkj\tsdfh")
    assert.deepStrictEqual(replaceSymbol("askjdhfkj\\sdfh", "\\", "\t"), "askjdhfkj\tsdfh")
    assert.deepStrictEqual(replaceSymbol("askjdhfkj\nsdfh", "\n", " "), "askjdhfkj sdfh")
}

function testreplaceSymbols() {
    assert.deepStrictEqual(replaceSymbols("abcdefg", ["a", "b"], "c"), "cccdefg")
}
    
function testisNumeric() {
    assert.deepStrictEqual(isNumeric("a"), false)
    assert.deepStrictEqual(isNumeric("%"), false)
    assert.deepStrictEqual(isNumeric("!"), false)
    assert.deepStrictEqual(isNumeric(";"), false)
    assert.deepStrictEqual(isNumeric("1"), true)
    assert.deepStrictEqual(isNumeric("2"), true)
    assert.deepStrictEqual(isNumeric("3"), true)
    assert.deepStrictEqual(isNumeric("4"), true)
    assert.deepStrictEqual(isNumeric("5"), true)
    assert.deepStrictEqual(isNumeric("6"), true)
    assert.deepStrictEqual(isNumeric("7"), true)
    assert.deepStrictEqual(isNumeric("8"), true)
    assert.deepStrictEqual(isNumeric("9"), true)
    assert.deepStrictEqual(isNumeric("0"), true)
    assert.deepStrictEqual(isNumeric("10"), false)
}

function testisAlpha() {
    assert.deepStrictEqual(isAlpha("a"), true)
    assert.deepStrictEqual(isAlpha("c"), true)
    assert.deepStrictEqual(isAlpha("z"), true)
    assert.deepStrictEqual(isAlpha("A"), true)
    assert.deepStrictEqual(isAlpha("C"), true)
    assert.deepStrictEqual(isAlpha("Z"), true)
    assert.deepStrictEqual(isAlpha("1"), false)
    assert.deepStrictEqual(isAlpha("7"), false)
    assert.deepStrictEqual(isAlpha("&"), false)
}

function testaddSpaceBetweenLettersAndNumbers() {
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("abc123"), "abc 123")
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("123abc"), "123 abc")
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("123456"), "123456")
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("abcdefg"), "abcdefg")
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("1A"), "1 A")
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("G1"), "G 1")
    assert.deepStrictEqual(addSpaceBetweenLettersAndNumbers("Z4"), "Z 4")
}

function testreplacePeriods() {
    assert.deepStrictEqual(replacePeriods("This is a sentence."), "This is a sentence ")
    assert.deepStrictEqual(replacePeriods("This is a sentence.Testing!"), "This is a sentence Testing!")
    assert.deepStrictEqual(replacePeriods("This is a 0.Testing!"), "This is a 0 Testing!")
    assert.deepStrictEqual(replacePeriods("This is a 0.1 Testing!"), "This is a 0.1 Testing!")
    assert.deepStrictEqual(replacePeriods("123.456.789"), "123.456 789")
    assert.deepStrictEqual(replacePeriods("123.456.789.012"), "123.456 789.012")
    assert.deepStrictEqual(replacePeriods("trying.this.out 123.456.789.012 123.456 123. and .123"), "trying this out 123.456 789.012 123.456 123  and  123")
}

function testlinearSearch() {
    assert.deepStrictEqual(linearSearch([], ""), false)
    assert.deepStrictEqual(linearSearch([], " "), false)
    assert.deepStrictEqual(linearSearch([1, 2, 3], 1), true)
    assert.deepStrictEqual(linearSearch([1, 2, 3], 2), true)
    assert.deepStrictEqual(linearSearch([1, 2, 3], 3), true)
    assert.deepStrictEqual(linearSearch([1, 2, 3], 4), false)
    assert.deepStrictEqual(linearSearch([""], " "), false)
    assert.deepStrictEqual(linearSearch([" "], " "), true)
    assert.deepStrictEqual(linearSearch(["a"], "b"), false)
    assert.deepStrictEqual(linearSearch(["a"], "a"), true)
    assert.deepStrictEqual(linearSearch(["b", "a"], "a"), true)
    assert.deepStrictEqual(linearSearch(["a", "b"], "a"), true)
    assert.deepStrictEqual(linearSearch(["a", "b", "c"], "d"), false)
    assert.deepStrictEqual(linearSearch(["a", "b", "c"], "c"), true)
    assert.deepStrictEqual(linearSearch(["\\", "SDKLFJ", "zxcklzxc"], "zxcklzxc"), true)
    assert.deepStrictEqual(linearSearch(["\\", "SDKLFJ", "zxcklzxc"], "\\"), true)
}

function testBinarySearch() {
    assert.deepStrictEqual(binarySearch([], ""), false)
    assert.deepStrictEqual(binarySearch([1, 2, 3], 0), false)
    assert.deepStrictEqual(binarySearch([1, 2, 3], 1), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3], 2), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3], 3), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3], 4), false)
    assert.deepStrictEqual(binarySearch([1, 2, 3], 0), false)
    assert.deepStrictEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 1), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 3), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 5), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 7), true)
    assert.deepStrictEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 0), false)
    assert.deepStrictEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 10), false)
}

function testUnique() {
    assert.deepStrictEqual(unique([]), [])
    assert.deepStrictEqual(unique(["a"]), ["a"])
    assert.deepStrictEqual(unique(["a", "a"]), ["a"])
    assert.deepStrictEqual(unique(["a", "b"]), ["a", "b"])
    assert.deepStrictEqual(unique(["a", "a", "a"]), ["a"])
    assert.deepStrictEqual(unique(["a", "a", "b"]), ["a", "b"])
    assert.deepStrictEqual(unique(["a", "aaa", "b"]), ["a", "aaa", "b"])
    assert.deepStrictEqual(unique(["a", "b", "c", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(unique(["a", "a", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(unique(["a", "a", "a", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(unique(["a", "a", "b", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(unique(["a", "b", "b", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(unique(["111", "b", "c", "c"]), ["111", "b", "c"])
}

function testDifference() {
    assert.deepStrictEqual(difference([], []), [])
    assert.deepStrictEqual(difference([1], []), [1])
    assert.deepStrictEqual(difference([], [1]), [])
    assert.deepStrictEqual(difference([], [1, 2, 3]), [])
    assert.deepStrictEqual(difference([1, 2, 3], []), [1, 2, 3])
    assert.deepStrictEqual(difference([1, 2, 3], [1, 2]), [3])
    assert.deepStrictEqual(difference([1, 2], [1, 2, 3]), [])
    assert.deepStrictEqual(difference([1, 2, 3], [1, 2, 3]), [])
    assert.deepStrictEqual(difference(["a", "b"], ["a", "b", "c"]), [])
    assert.deepStrictEqual(difference(["b", "c"], ["a", "b", "c"]), [])
    assert.deepStrictEqual(difference(["a", "c"], ["a", "b", "c"]), [])
    assert.deepStrictEqual(difference(["a", "b", "c"], ["a", "b"]), ["c"])
    assert.deepStrictEqual(difference(["a", "b", "c"], ["b", "c"]), ["a"])
    assert.deepStrictEqual(difference(["a", "b", "c"], ["a", "c"]), ["b"])
    assert.deepStrictEqual(difference(["a", "b", "c"], ["a", "c", "d"]), ["b"])
    assert.deepStrictEqual(difference(["bee", "bumble"], ["bee", "bumble", "buzz"]), [])
    assert.deepStrictEqual(difference(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]), ["bliss"])
    assert.deepStrictEqual(difference(["alpha", "beta", "omega"], ["alpha", "beta"]), ["omega"])
    assert.deepStrictEqual(difference(["alpha", "beta", "omega"], ["beta", "omega"]), ["alpha"])
}

function testUnion() {
    assert.deepStrictEqual(union([], []), [])
    assert.deepStrictEqual(union([1], []), [1])
    assert.deepStrictEqual(union([], [1]), [1])
    assert.deepStrictEqual(union([], [1, 2, 3]), [1, 2, 3])
    assert.deepStrictEqual(union([1, 2, 3], []), [1, 2, 3])
    assert.deepStrictEqual(union([1, 2, 3], [1, 2]), [1, 2, 3])
    assert.deepStrictEqual(union([1, 2], [1, 2, 3]), [1, 2, 3])
    assert.deepStrictEqual(union([1, 2, 3], [1, 2, 3]), [1, 2, 3])
    assert.deepStrictEqual(union(["a", "b"], ["a", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(union(["b", "c"], ["a", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(union(["a", "c"], ["a", "b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(union(["a", "b", "c"], ["a", "b"]), ["a", "b", "c"])
    assert.deepStrictEqual(union(["a", "b", "c"], ["b", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(union(["a", "b", "c"], ["a", "c"]), ["a", "b", "c"])
    assert.deepStrictEqual(union(["bee", "bumble"], ["bee", "bumble", "buzz"]), ["bee", "bumble", "buzz"])
    assert.deepStrictEqual(union(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]), ["bee", "bliss", "bumble", "buzz"])
    assert.deepStrictEqual(union(["alpha", "beta"], ["alpha", "beta", "omega"]), ["alpha", "beta", "omega"])
    assert.deepStrictEqual(union(["beta", "omega"], ["alpha", "beta", "omega"]), ["alpha", "beta", "omega"])
}

function testIntersection() {
    assert.deepStrictEqual(intersection([], []), []);
    assert.deepStrictEqual(intersection([1], []), []);
    assert.deepStrictEqual(intersection([], [1]), []);
    assert.deepStrictEqual(intersection([], [1, 2, 3]), []);
    assert.deepStrictEqual(intersection([1, 2, 3], []), []);
    assert.deepStrictEqual(intersection([1, 2, 3], [1, 2]), [1, 2]);
    assert.deepStrictEqual(intersection([1, 2], [1, 2, 3]), [1, 2]);
    assert.deepStrictEqual(intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3]);
    assert.deepStrictEqual(intersection(["a", "b"], ["a", "b", "c"]), ["a", "b"]);
    assert.deepStrictEqual(intersection(["b", "c"], ["a", "b", "c"]), ["b", "c"]);
    assert.deepStrictEqual(intersection(["a", "c"], ["a", "b", "c"]), ["a", "c"]);
    assert.deepStrictEqual(intersection(["a", "b", "c"], ["a", "b"]), ["a", "b"]);
    assert.deepStrictEqual(intersection(["a", "b", "c"], ["b", "c"]), ["b", "c"]);
    assert.deepStrictEqual(intersection(["a", "b", "c"], ["a", "c"]), ["a", "c"]);
    assert.deepStrictEqual(intersection(["bee", "bumble"], ["bee", "bumble", "buzz"]), ["bee", "bumble"]);
    assert.deepStrictEqual(intersection(["bee", "bliss", "bumble"], ["bee", "bumble", "buzz"]), ["bee", "bumble"]);
    assert.deepStrictEqual(intersection(["alpha", "beta"], ["alpha", "beta", "omega"]), ["alpha", "beta"]);
    assert.deepStrictEqual(intersection(["beta", "omega"], ["alpha", "beta", "omega"]), ["beta", "omega"]);
}

function testSetOps() {
    function generateSetOpsCmd(set1, set2, operation) {
        return `node setops.js "set1=${set1};set2=${set2};operation=${operation}"`;
    }
    
    function readOutputTxt() {
        return fs.readFileSync('result.txt', 'utf8');
    }
    
    function readTxt(filepath) {
        return fs.readFileSync(filepath, 'utf8');
    }
    
    function runTest(set1, set2, operation, answer) {
        childProcess.execSync(generateSetOpsCmd(set1, set2, operation));
        const output = readOutputTxt();
        const expected = removeSymbol(readTxt(answer), "\r");
        assert.deepStrictEqual(output, expected);
    }
    
    runTest("./test/a.txt", "./test/b.txt", "intersection", "./test/a_b_intersection.txt");
    runTest("./test/a.txt", "./test/b.txt", "union", "./test/a_b_union.txt");
    runTest("./test/a.txt", "./test/b.txt", "difference", "./test/a_b_difference.txt");
    
    runTest("./test/c.txt", "./test/d.txt", "intersection", "./test/c_d_intersection.txt");
    runTest("./test/c.txt", "./test/d.txt", "union", "./test/c_d_union.txt");
    runTest("./test/c.txt", "./test/d.txt", "difference", "./test/c_d_difference.txt");
    
    runTest("./test/e.txt", "./test/f.txt", "intersection", "./test/e_f_intersection.txt");
    runTest("./test/e.txt", "./test/f.txt", "union", "./test/e_f_union.txt");
    
    runTest("./test/g.txt", "./test/h.txt", "intersection", "./test/g_h_intersection.txt");
    runTest("./test/g.txt", "./test/h.txt", "union", "./test/g_h_union.txt");
    
    runTest("./test/a1.txt", "./test/b1.txt", "intersection", "./test/result1.txt");
    runTest("./test/a2.txt", "./test/b2.txt", "difference", "./test/result2.txt");
    runTest("./test/a3.txt", "./test/b3.txt", "union", "./test/result3.txt");
    runTest("./test/a4.txt", "./test/b4.txt", "intersection", "./test/result4.txt");
    
    runTest("./test/testcase1.txt", "./test/testcase2.txt", "intersection", "./test/testcase1_testcase2_intersection.txt");
    runTest("./test/testcase1.txt", "./test/testcase2.txt", "difference", "./test/testcase1_testcase2_difference.txt");
    runTest("./test/testcase1.txt", "./test/testcase2.txt", "union", "./test/testcase1_testcase2_union.txt");
}

testisSortedAsc()
testsort()
testdelimiter()
testremoveSymbol()
testtoLower()
testreplaceSymbol()
testreplaceSymbols()
testisNumeric()
testisAlpha()
testaddSpaceBetweenLettersAndNumbers()
testreplacePeriods()
testlinearSearch()
testBinarySearch()
testUnique()
testDifference()
testUnion()
testIntersection()
testSetOps()
