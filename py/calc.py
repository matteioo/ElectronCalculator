import math

vars = {}

def interpret(input_string):
    help = 'ya wish'
    if(input_string == 'help'):
        return help
    else:
        if 'var:' in input_string:
            input_string = var_handling(input_string)
        if '=' in input_string:
            exec(cleanup(input_string))
            return str(eval(input_string[:input_string.find('=')]))
        else: return str(eval(cleanup(input_string)))


def cleanup(input_string):
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
    while 'var:' in input_string:
        var_index = input_string.find(':')
        input_string = input_string.replace('var:', 'vars[\'')
        input_string = input_string[:var_index+4] + '\']' + input_string[var_index+4:]
    return input_string
