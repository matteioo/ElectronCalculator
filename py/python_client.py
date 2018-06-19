import zerorpc

# this is modified (stolen) example code

def main():
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")
    print('conn')
    while True:
        print(c.expression_handling(input('>')))

if __name__ == '__main__':
    main()
