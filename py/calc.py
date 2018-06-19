import math

vars = {}   # all variables are stored here

def interpret(input_string):
     # because of my way to deal with ambiguity, a space must be added to the start of the string
    input_string = " " + input_string
    """interprets a string as algebraic expression, specifics in README.md"""
    help = 'ya wish'    # gotta actually write this...
    if(input_string == 'help'):
        return help
    else:
        if 'var:' in input_string:
            input_string = var_handling(input_string)
        if '=' in input_string:
            exec(cleanup(input_string))     # exec is used to store variables
            return str(eval(input_string[:input_string.find('=')]))
        else: return str(eval(cleanup(input_string)))


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
        input_string = input_string.replace('var:', 'vars[\'')
        input_string = input_string[:var_index+4] + '\']' + input_string[var_index+4:]
    return input_string
