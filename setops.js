const fs = require('fs');

function isSortedAsc(sortedList) {
    if (sortedList.length <= 1) {
        return true;
    }
    if (sortedList[0] > sortedList[1]) {
        return false;
    }
    return isSortedAsc(sortedList.slice(1));
}

function delimiter(string, symbol) {
    if (!string) {
        return [];
    }
    const symbolString = symbol + string;
    return _delimiterHelperNext(symbolString, symbol);
}

function _delimiterHelperGetWord(string, symbol) {
    if (!string || string[0] === symbol) {
        return "";
    }
    return string[0] + _delimiterHelperGetWord(string.slice(1), symbol);
}

function _delimiterHelperNext(string, symbol) {
    if (!string) {
        return [];
    }
    if (string.length > 1 && string[0] === symbol && string[1] !== symbol) {
        return [_delimiterHelperGetWord(string.slice(1), symbol), ..._delimiterHelperNext(string.slice(1), symbol)];
    }
    return _delimiterHelperNext(string.slice(1), symbol);
}

function removeSymbol(string, symbol) {
    if (!string) {
        return "";
    }
    if (string[0] === symbol) {
        return removeSymbol(string.slice(1), symbol);
    }
    return string[0] + removeSymbol(string.slice(1), symbol);
}

function removeSymbols(string, symbols) {
    if (!symbols.length) {
        return string;
    }
    return removeSymbols(removeSymbol(string, symbols[0]), symbols.slice(1));
}

function toLower(string) {
    if (!string) {
        return "";
    }
    if (65 <= string.charCodeAt(0) && string.charCodeAt(0) <= 90) {
        return String.fromCharCode(string.charCodeAt(0) + 32) + toLower(string.slice(1));
    }
    return string[0] + toLower(string.slice(1));
}

function linearSearch(list, element) {
    if (!list.length) {
        return false;
    }
    if (list[0] === element) {
        return true;
    }
    return linearSearch(list.slice(1), element);
}

function _binarySearchHelper(sortedList, element) {
    if (!sortedList.length) {
        return false;
    }
    if (sortedList[Math.floor(sortedList.length / 2)] === element) {
        return true;
    }
    if (sortedList[Math.floor(sortedList.length / 2)] < element) {
        return _binarySearchHelper(sortedList.slice(Math.floor(sortedList.length / 2) + 1), element);
    }
    return _binarySearchHelper(sortedList.slice(0, Math.floor(sortedList.length / 2)), element);
}

function binarySearch(sortedList, element) {
    if (!isSortedAsc(sortedList)) {
        throw new Error("list must be sorted to call binary search function");
    }
    return _binarySearchHelper(sortedList, element);
}

function replaceSymbol(string, oldSymbol, newSymbol) {
    if (!string) {
        return "";
    }
    if (string[0] === oldSymbol) {
        return newSymbol + replaceSymbol(string.slice(1), oldSymbol, newSymbol);
    }
    return string[0] + replaceSymbol(string.slice(1), oldSymbol, newSymbol);
}

function replaceSymbols(string, oldSymbols, newSymbol) {
    if (!string) {
        return "";
    }
    if (!oldSymbols.length) {
        return string;
    }
    return replaceSymbols(replaceSymbol(string, oldSymbols[0], newSymbol), oldSymbols.slice(1), newSymbol);
}

function _uniqueHelper(sortedList, currEl) {
    if (!sortedList.length) {
        return [];
    }
    if (sortedList[0] === currEl) {
        return _uniqueHelper(sortedList.slice(1), currEl);
    }
    return [sortedList[0], ..._uniqueHelper(sortedList.slice(1), sortedList[0])];
}

function unique(sortedList) {
    if (!isSortedAsc(sortedList)) {
        throw new Error("list must be sorted to call unique function");
    }
    if (!sortedList.length) {
        return [];
    }
    return [sortedList[0], ..._uniqueHelper(sortedList.slice(1), sortedList[0])];
}

function _merge(l1, l2) {
    if (!l1.length) {
        return l2;
    }
    if (!l2.length) {
        return l1;
    }
    if (l1[0] <= l2[0]) {
        return [l1[0], ..._merge(l1.slice(1), l2)];
    }
    return [l2[0], ..._merge(l1, l2.slice(1))];
}

function _mergeSort(l) {
    if (l.length <= 1) {
        return l;
    }
    return _merge(_mergeSort(l.slice(0, Math.floor(l.length / 2))), _mergeSort(l.slice(Math.floor(l.length / 2))));
}

function sort(l) {
    return _mergeSort(l);
}

function _differenceHelper(sortedSet1, sortedSet2) {
    if (!sortedSet1.length) {
        return [];
    }
    if (!sortedSet2.length) {
        return sortedSet1;
    }
    if (sortedSet1[0] === sortedSet2[0]) {
        return _differenceHelper(sortedSet1.slice(1), sortedSet2.slice(1));
    }
    if (sortedSet1[0] < sortedSet2[0]) {
        return [sortedSet1[0], ..._differenceHelper(sortedSet1.slice(1), sortedSet2)];
    }
    return _differenceHelper(sortedSet1, sortedSet2.slice(1));
}

function difference(sortedSet1, sortedSet2) {
    if (!isSortedAsc(sortedSet1) || !isSortedAsc(sortedSet2)) {
        throw new Error("list must be sorted to call set difference function");
    }
    return sort(_differenceHelper(sortedSet1, sortedSet2));
}

function union(sortedSet1, sortedSet2) {
    if (!isSortedAsc(sortedSet1) || !isSortedAsc(sortedSet2)) {
        throw new Error("list must be sorted to call set union function");
    }
    return unique(sort([...sortedSet1, ...sortedSet2]));
}

function _intersectionHelper(sortedSet1, sortedSet2) {
    if (!sortedSet1.length || !sortedSet2.length) {
        return [];
    }
    if (sortedSet1[0] === sortedSet2[0]) {
        return [sortedSet1[0], ..._intersectionHelper(sortedSet1.slice(1), sortedSet2.slice(1))];
    }
    if (sortedSet1[0] < sortedSet2[0]) {
        return _intersectionHelper(sortedSet1.slice(1), sortedSet2);
    }
    return _intersectionHelper(sortedSet1, sortedSet2.slice(1));
}

function intersection(sortedSet1, sortedSet2) {
    if (!isSortedAsc(sortedSet1) || !isSortedAsc(sortedSet2)) {
        throw new Error("list must be sorted to call set intersection function");
    }
    return sort(_intersectionHelper(sortedSet1, sortedSet2));
}

function isAlpha(string) {
    if (string.length !== 1) {
        return false;
    }
    return binarySearch("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", string);
}

function isNumeric(string) {
    if (string.length !== 1) {
        return false;
    }
    return binarySearch("0123456789", string);
}

function generateBooleanArray(n) {
    if (n === 0) {
        return [];
    }
    return [false, ...generateBooleanArray(n - 1)];
}

function _markIsCompletedNumber(string, isCompletedNumber) {
    if (!isCompletedNumber.length) {
        return [];
    }
    if (isNumeric(string[0])) {
        return [true, ..._markIsCompletedNumber(string.slice(1), isCompletedNumber.slice(1))];
    }
    return isCompletedNumber;
}

function _replacePeriodsHelper(string, isCompletedNumber) {
    if (string.length < 3) {
        return string;
    }
    if (string[1] === "." && (isNumeric(string[0]) && isNumeric(string[2])) && !isCompletedNumber[0]) {
        return string[0] + _replacePeriodsHelper(string.slice(1), [false, ..._markIsCompletedNumber(string.slice(2), isCompletedNumber.slice(2))]);
    }
    if (string[1] === ".") {
        return string[0] + _replacePeriodsHelper(" " + string.slice(2), isCompletedNumber.slice(1));
    }
    return string[0] + _replacePeriodsHelper(string.slice(1), isCompletedNumber.slice(1));
}

function replacePeriods(string) {
    if (!string) {
        return "";
    }
    return _replacePeriodsHelper(" " + string + " ", generateBooleanArray(string.length)).slice(1, -1);
}

function addSpaceBetweenLettersAndNumbers(string) {
    if (!string) {
        return "";
    }
    if (string.length < 2) {
        return string;
    }
    if ((isAlpha(string[0]) && isNumeric(string[1])) || (isNumeric(string[0]) && isAlpha(string[1]))) {
        return string[0] + " " + addSpaceBetweenLettersAndNumbers(string.slice(1));
    }
    return string[0] + addSpaceBetweenLettersAndNumbers(string.slice(1));
}

function stringToSortedWordSet(string) {
    const cleanedString = addSpaceBetweenLettersAndNumbers(
            replacePeriods(
                    replaceSymbols(
                        string, 
                        ["!", "?", "'", "\"", ",", "/", "\\", "~", "-","(", ")", 
                        "\n", "\t", "\r", ";", ":", "[", "]", "{", "}", "+", "-", 
                        "&", "*", "%", "$", "@", "#", "^", "_", "=", "`", "<", ">", "|"], 
                        " "
                    )
                )
            );
    const wordList = delimiter(cleanedString, " ").map(toLower);
    return unique(sort(wordList));
}

function getCliInput() {
    const args = process.argv.slice(2);
    if (args.length !== 1) {
        console.log("Usage: node script.js \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"");
        process.exit(1);
    }

    const textCLIArgs = args[0];
    const varList = delimiter(textCLIArgs, ";");

    if (varList.length !== 3) {
        console.log("Usage: node setops.js \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"");
        process.exit(1);
    }

    const filepath1 = delimiter(varList[0], "=");
    const filepath2 = delimiter(varList[1], "=");
    const operation = delimiter(varList[2], "=");

    if (filepath1.length !== 2 || filepath2.length !== 2 || operation.length !== 2) {
        console.log("Usage: node setops.js \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"");
        process.exit(1);
    }

    if (!(operation[1] === "difference" || operation[1] === "union" || operation[1] === "intersection")) {
        console.log("Usage: node setops.js \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"");
        process.exit(1);
    }

    return [filepath1[1], filepath2[1], operation[1]];
}

function resultToStringHelper(results) {
    if (!results.length) {
        return "";
    }
    return "\n" + results[0] + resultToStringHelper(results.slice(1));
}

function resultToString(results) {
    if (!results.length) {
        return "empty set";
    }
    return results[0] + resultToStringHelper(results.slice(1));
}

function writeOutput(results) {
    fs.writeFileSync("result.txt", resultToString(results));
}

function main() {
    const [filepath1, filepath2, operation] = getCliInput();

    try {
        const text1 = fs.readFileSync(filepath1, 'utf8');
        const text2 = fs.readFileSync(filepath2, 'utf8');

        if (operation === "difference") {
            writeOutput(difference(stringToSortedWordSet(text1), stringToSortedWordSet(text2)));
        } else if (operation === "union") {
            writeOutput(union(stringToSortedWordSet(text1), stringToSortedWordSet(text2)));
        } else if (operation === "intersection") {
            writeOutput(intersection(stringToSortedWordSet(text1), stringToSortedWordSet(text2)));
        }
    } catch (error) {
        console.error(error.message);
        process.exit(1);
    }
}


if (require.main === module) {
    main();
} else {
    module.exports = {
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
    };
}
