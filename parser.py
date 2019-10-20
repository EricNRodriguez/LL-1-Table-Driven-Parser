from invalid_symbol_error import InvalidSymbolError
from ll1_table import terminals, table
from sys import argv

class Parser():

    def __init__(self, table, terminals):
        self.table = table
        self.variables = list(table.keys())
        self.terminals = terminals # make this simple, and just find the lowercase things

    def get_terminals(self):
        return self.terminals

    def get_variables(self):
        return self.variables

    def __format_string(self, string):
        return string.replace(' ', '').replace('\n', '') + '$'

    def validate(self, string):
        string = self.__format_string(string)

        if len(list(filter(lambda input_char : input_char not in self.terminals, string[:len(string)-1]))) != 0:
            raise InvalidSymbolError("ERROR_INVALID_SYMBOL")

        stack = ["$", "S"]
        for i, char in enumerate(string):

            print('{:<25}        {}'.format(string[i:], ''.join(stack[::-1])))

            if len(stack) == 0:
                return False # unread input

            # apply production rules until top of stack is no longer a variable
            while stack[-1] in self.variables:
                production = self.table[stack[-1]].get(char, None)
                if production is None:
                    return False
                else:
                    stack.pop()
                    # push right hand side of productions to stack, ignore '' (epsilon)
                    stack.extend(list(filter(lambda alpha : alpha != '', production))[::-1])

                print('{:<25}        {}'.format(string[i:], ''.join(stack[::-1])))

            if stack[-1] in self.terminals and stack[-1] == char:
                stack.pop()
            else:
                return stack[-1] == char and stack[-1] == '$' and stack[-1] not in self.terminals

        return False




def main():

    if len(argv) < 2:
        print(" File path to string required as argument")
        quit()

    parser = Parser(table, terminals)

    try:
        string = open(argv[1]).read().replace('\n', '').replace(" ", "")
    except FileNotFoundError as e:
        print("Invalid file path")
        quit()
    except Exception as e:
        print(e.__repr__())
        quit()

    try:
        print("ACCEPTED") if parser.validate(string) else print("REJECTED")
    except InvalidSymbolError as e:
        print(e.__str__())
    except Exception as e:
        print(e.__repr__())
    return

if __name__ == '__main__':
   main()
