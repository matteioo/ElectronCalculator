import sys
import math

vars = {}   # all variables are stored here
ans = 0

def interpret(input_string):
    """interprets a string as algebraic expression, specifics in README.md"""
    global ans
     # because of my way to deal with ambiguity, a space must be added to the start of the string
    input_string = " " + input_string
    help = 'ya wish'    # gotta actually write this...
    if(input_string == 'help'):
        return help
    elif input_string == ' ':
        return ''
    elif input_string[1:7] == 'delete': #if a 'delete' occurs, it must be leading, and dont forget the added ' '
        delete_var(input_string[12])
        return ''
    elif input_string[1:8] == 'varlist':
        return list_var()
    elif input_string[1:8] == 'varwipe':
        wipe_var()
        return ''
    else:
        if 'var:' in input_string:
            try:
                input_string = var_handling(input_string)
            except AssertionError:
                return 'Varname too long, max is 1 char'
            except:
                return ('[22] Generic Error' + str(sys.exc_info()[0]))
        if '=' in input_string:
            try:
                exec(cleanup(input_string)[1:])     # exec is used to store variables, the space from line 9 hast to be removed again
            except KeyError:
                return 'Unknown variable name'
            except SyntaxError:
                return 'Unrecognised Expression - more than one variable on the left side of \'=\'?'
            except:
                return ('[0] Generic Error' + str(sys.exc_info()[0]))
            try:
                ans = eval(input_string[:input_string.find('=')])
            except ZeroDivisionError:
                return 'Division by Zero'
            except NameError:
                return 'Unrecognised expression - NaN somewhere?'
            except:
                return ('[1] Generic Error' + str(sys.exc_info()[0]))
            return str(ans)
        else:
            try:
                ans = eval(cleanup(input_string))
            except ZeroDivisionError:
                return 'Division by Zero'
            except NameError:
                return 'NaN somewhere?'
            except SyntaxError:
                return 'Unrecognised expression - maybe parantheses mismatch or unrecognised symbol?'
            except KeyError:
                return 'Unknown variable name'
            except:
                return ('[2] Generic Error' + str(sys.exc_info()[0]))
            return str(ans)


def cleanup(input_string):
    """transforms a more 'casual' expression to one python can understand"""
    # the spaces in the list are necessary to avoid ambiguity
    # example: without spaces, cleanup() would turn math.sin into math.math.sin
    to_replace = [' root', ' ln', ' log', ' sin', ' tan', ' cos', ' asin', ' acos',
                  ' atan', ' pi', ' e', '^', '²', '³', '⁴']
    replaced_by = [' math.sqrt', ' math.log', ' math.log10', ' math.sin',
                   ' math.cos', ' math.tan', ' math.asin', ' math.acos',
                   ' math.atan', ' math.pi', ' math.e', '**',
                   '**2', '**3', '**4']

    for i in range(len(to_replace)):
        if to_replace[i] in input_string:
            while(to_replace[i] in input_string):
                input_string = input_string.replace(to_replace[i], replaced_by[i])
    return input_string

def var_handling(input_string):
    """handles variables, each variable is stored in the vars dict, the name is limited to 1 char"""
    while 'var:' in input_string:
        var_index = input_string.find(':')
        #assert input_string[var_index+2] == ' ', 'varname to long'
        input_string = input_string.replace('var:', 'vars[\'', 1)
        input_string = input_string[:var_index+4] + '\']' + input_string[var_index+4:]
    #if input_string[-3] == '[': input_string = input_string + '\']' # easyfix for wierd bug
    return input_string

def delete_var(key):
    """deletes one variable"""
    del vars[key]
    return

def list_var():
    """lists all variables"""
    return str(vars)

def wipe_var():
    """deletes all varables"""
    global vars
    vars = {}
    return

def main():
    return interpret(sys.argv[1])

print(main())
