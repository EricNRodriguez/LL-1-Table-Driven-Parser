class Parser():

    def __init__(self, table, terminals):
        self.table = table
        self.variables = list(table.keys())
        self.terminals = terminals


    def parse_string(self, string):
        stack = ["$", "S"]

        for char in string+"$":

            if len(stack) == 0:
                return False #unread input

            # apply production rules until top of stack is no longer a variable
            while stack[-1] in self.variables:
                production = self.table[stack[-1]].get(char, None)

                if production is None:
                    print("production was None | Char --> ", char, " | Stack -->", stack[-1])
                    return False
                else:
                    stack.pop()
                    for alpha in production[::-1]:
                        if alpha != '': stack.append(alpha)

            if stack[-1] in self.terminals:
                if stack[-1] == char:
                    stack.pop()
                else:
                    return False # terminal in stack and input dont match
            else:
                if stack[-1] == char and stack[-1] == '$':
                    return True
                else:
                    return False

        return True
