# Running the Program
This homework assignment is a collection of two scripts: `setops.js` and `setops.py`. They both accomplish the same things, as tasked in the homework description. To run the program, run the following command(s):

* For Python: `python3 setops.py "set1=[filename];set2=[filename];operation=[difference|union|intersection]"`

* For JavaScript: `node setops.js "set1=[filename];set2=[filename];operation=[difference|union|intersection]"`

For example,
* `python3 setops.py "set1=./test/a1.txt;set2=./test/b1.txt;operation=intersection"`
* `node setops.js "set1=./test/a1.txt;set2=./test/b1.txt;operation=intersection"`

Results can be found in the `result.txt` file in the root directory. They are structured with each unique word on a new line.

# Description
This is a program that computes set operations on files with words and numbers. This is a primitive storage mechanism used everywhere, including search engines and word processors.

The input consists of two files and one set operation to execute (difference, union, intersection).

# Running Unit Tests
Two sets of unit tests are supplied. To run the test simply run the following commands:

* For Python: `python3 test.py`

* For JavaScript: `node test.js`

# Opinion on JavaScript vs. Python
From a functional programming perspective, they are fairly similar. They both have built-in lambda and higher-order functions. They both support recursion (as with any modern language,) and have dynamic data types.

However, the key difference is difficulty of memory management in JavaScript compared to Python. In Python, it is more comfortable to know when using certain operators that the data structure has been completed cloned. In JavaScript, shallow copies are the norm rather than the exception when dealing with objects (e.g. `array.prototype.slice()` returns a "shallow copy"), so it can be rather difficult to keep track of memory. However, since this project involved not mutating any memory at all, it was not an issue. It is just something to keep in mind.

In addition, JavaScript (Node.js) is [asynchronous I/O by default](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs). In Python, asynchronous methods are kept in the asyncio module, whereas in JavaScript they can be everywhere (for example, `writeFileSync` vs. `writeFile` and `fetch`). 

Overall, I enjoy Python more since asynchronous behaviour is not the default for I/O, and the syntax is elegant to me (don't get me started on JavaScript callback hell syntax.) If asynchronous behaviour is desired, you would wrap functions with the asyncio module, which makes more sense to me. However, I understand doing so can be verbose and that a developer could want asynchronous I/O to be the default, especially on web applications.