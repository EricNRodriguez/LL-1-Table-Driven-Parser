#!/usr/bin/env
from parser import Parser

if __name__ == '__main__':

    # LL(1) parse table
    table = {
        "S" : {
            **dict.fromkeys(["(", "x", "y", "z", "1","2","3","4","5","6","7","8","9", "l", "w"], ["L","S"]),
            **dict.fromkeys(["i", ";", "$"], [""]),
        },
        "L" : {
            **dict.fromkeys(["(", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ["E",";"]),
            **{"l" : "A;", "w" : "C;", },
        },
        "E" : {
            **{"(" : list("(EBE)")},
            **dict.fromkeys(["x", "y", "z"], ["V"]),
            **dict.fromkeys(["1","2","3","4","5","6","7","8","9"], ["N"]),
        },
        "A" : {
            "l" : list("letV=E"),
        },
        "C" : {
            "w" : list("whileEdoSF"),
        },
        "F" : {
            "e" : list("else S"),
            ";" : [""],
        },
        "B" : {
            "+" : ["+"],
            "-" : ["-"],
            "*" : ["*"],
            ">" : [">"],
        },
        "V" : {
            "x" : ["x"],
            "y" : ["y"],
            "z" : ["z"],
        },
        "N" : dict.fromkeys(["1","2","3","4","5","6","7","8","9"], ["D","G"]),
        "G" : {
            **dict.fromkeys(["1","2","3","4","5","6","7","8","9", "0"], ["D","G"]),
            **dict.fromkeys(["0"], ["0", "G"]),
            **dict.fromkeys(['+', '-', '*', '>', ')', ';', 'd'], ""), # sketchy - added without thinking
        },
        "D" : {
            "1" : ["1"],
            "2" : ["2"],
            "3" : ["3"],
            "4" : ["4"],
            "5" : ["5"],
            "6" : ["6"],
            "7" : ["7"],
            "8" : ["8"],
            "9" : ["9"],
        }
    }

    parser = Parser(table, ["0", "1", "t","2", "3", "=",'8', ";","4", "5", "6", 'z', 'i', "7", "8", "9", '*', '6', ';', 'x',
                            '3', 'w', 'e', 'y', '+', '(', '7', '>', '5', 'l', '1', '2', '9', '-', '4',")", *list("else S"),
                            *list("else S"), *list("whileEdoSF")])
    try:
        print("ACCEPTED") if parser.validate("(x+1);") else print("REJECTED")
    except Exception as e:
        print(e)

    try:
        print("ACCEPTED") if parser.validate("") else print("REJECTED")
    except Exception as e:
        print(e)

    try:
        print("ACCEPTED") if parser.validate("letx = (y - 20);while 1 do y;;") else print("REJECTED")
    except Exception as e:
        print(e)

    try:
        print("ACCEPTED") if parser.validate("(x+1));") else print("REJECTED")
    except Exception as e:
        print(e)



    #"while(x>3)33doletx=(x+2);;" breaks it



