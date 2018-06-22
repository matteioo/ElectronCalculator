# [calc.py](calc.py)
## Description
This script contains functions to interpret algebraic expressions. It can also store and use variables. It actually evaluates Python statements, and translates statements python cannot interpret. So all Python operators are available, though you should stick to arithmetic operators. When writing inputs for this script, be generous with spaces and parentheses.

These expressions are usable:
  - [Python operators](https://www.tutorialspoint.com/python/python_basic_operators.htm)
  (Be aware that you should stick to arithmetic operators, but you don't _have_ to)
  - ^: exponentiation
  - ²,³,⁴: added for convenience
  - root: square root
  - ln: natural log
  - log: log base 10
  - sin, con, tan: trigonometric functions
  - asin, acos, atan: reverse trig functions
  - pi, e: constants
  - var:x : Store values in variables, they can be used at any time. Names are limited to 1 character

Example Expressions :
```
(4 * 3³ - sin(7 * pi) + root(7)) - 2^4
var:a = 5*7²
100 * pi + 6 / var:a
```

## Changelog
### v0.1
  - wrote script, with minimal testing
  - base features: basic variables, basic operations

### v0.2
  - cleaned up code
  - added comments

### v0.3
  - fixed Bug #1: leading function (e.g. log) cause errors

### v0.4
  - added ans functionality
  - added exception handling
    - Detect invalid variable names
    - Detect NaN inputs
    - Detect division by 0
  - fixed Bug #2: variables are broken
  - fixed Bug #3: multiple vars in one input do not work

### v0.4.1
  - added more exceptions with feedback
    - Detect Syntax Errors
    - Handle empty inputs

### v0.5
  - added 'listing' and 'delete' functionality to var system

### v0.6
  - removed zerorpc

## Bugs
  - Bug #1: leading function (e.g. log) cause errors.
    - Cause: Ambiguity handling demands a leading space for functions (e.g. log).
    - Fix: Add leading spaces to every input
  - Bug #2: variables are broken.
    - Cause: Leading space from bug-fix #1 caused exec() to fail due to incorrect indentation.
    - Fix: remove leading space before exec()
  - Bug #3: multiple vars in one input do not work
    - Cause: The opening brace for the vars dictionary is created by str.replace(), while the closing brace is placed using str.find(). After the first replace, find() cannot find its reference point
    - Fix: set max replaces per cycle to 1


# [test_calc.py](test_calc.py)
## Description
This is a test script for [calc.py](calc.py). It repeadetly calls interpret() from [calc.py](calc.py), in an endless loop. Variables and a few expressions were successfully tested.

Example:
```
>(4 * 3³ - sin(7 * pi) + root(7)) - 2^4
94.64576131106459
```
## Changelog
### v0.1
  - wrote script

# [api.py](api.py)
## Description
This script uses [zerorpc](http://www.zerorpc.io/) in conjunction with [calc.py](calc.py). In the future, this will be used to communicate with ~~insert app name here~~ the node.js app.  **This has been removed**
## Changelog
### v0.1
- worte script

# [python_client.py](python_client.py)
## Description
This script tests [api.py](api.py) by sending an input string to [api.py](api.py) and recieveing the processed input back. All working as expected. **This has been removed**
## Changelog
### v0.1
- wrote script

# [cli_calc.py](cli_calc.py)
## Description
This scripts calls interpret() from [calc.py](calc.py) on its argument. This was turned into an standalone executable using pyinstaller.
## Changelog
### v0.1
- wrote script
### vo.2
- copied all function definitions of [calc.py](calc.py) into this file in order to fix compilation - did not work
