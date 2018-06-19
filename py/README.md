# calc.py
## Description
This script contains functions to interpret algebraic expressions. It can also
store and use variables.
These expressions are usable:
  - (gonna do it soon, i promise)

Example Expressions :
```
(4 * 3³ - sin(7 * pi) + root(7)) - 2^4
var:a = 5*7²
100 * pi + 6 / var.a
```

## Changelog
### v0.1
  - wrote script, with minimal testing
### v0.2
  - cleaned up code
  - added comments
### v0.3
  - fixed bug: leading function (e.g. log) cause errors

# test_calc.py
##Description
This is a test script for calc.py. It repeadetly calls interpret() from calc.py, in an endless loop. Variables and a few expressions were successfully tested.

Example:
```
>(4 * 3³ - sin(7 * pi) + root(7)) - 2^4
94.64576131106459
```
## Changelog
### v0.1
  - wrote script

# api.py
## Description
This script uses zerorpc in conjunction with calc.py. In the future, this will be used to communicate with the node.js app.
## Changelog
### v0.1
- worte script

# python_client.py
## Description
This script tests api.py by sending an input string to api.py and recieveing the processed input back. All working as expected.
## Changelog
### v0.1
- wrote script
