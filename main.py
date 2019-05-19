#################################################
#The following is an interpreter in Python. This interpreter was created to detect syntax errors, report uninitialized variables and perform the assignments if there is no error and print out the values of all the variables after all the assignments are done.
#################################################
import sys
import lexer
import parser
import interpreter

def main():
    import sys
    text = open(sys.argv[0],'r').read()

    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    print(interpreter.GLOBAL_SCOPE)


if __name__ == '__main__':
    main()