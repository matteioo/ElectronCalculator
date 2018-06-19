import zerorpc
from calc import *

# this is modified (stolen) example code

class api(object):
    def expression_handling(self, input_string):
        output_string = interpret(input_string)
        return output_string

def main():
    s = zerorpc.Server(api())
    s.bind("tcp://0.0.0.0:4242")
    s.run()

if __name__ == '__main__':
    main()
