table = {
        "S": {
            **dict.fromkeys(["(", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "l", "w"], ["L", "S"]),
            **dict.fromkeys(["e", ";", "$"], [""]),
        },
        "L": {
            **dict.fromkeys(["(", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ["E", ";"]),
            **{"l": "A;", "w": ["C", ";"], },
        },
        "E": {
            **{"(": list("(EBE)")},
            **dict.fromkeys(["x", "y", "z"], ["V"]),
            **dict.fromkeys(["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["N"]),
        },
        "A": {
            "l": list("letV=E"),
        },
        "C": {
            "w": list("whileEdoSF"),
        },
        "F": {
            "e": list("elseS"),
            ";": [""],
        },
        "B": {
            "+": ["+"],
            "-": ["-"],
            "*": ["*"],
            ">": [">"],
        },
        "V": {
            "x": ["x"],
            "y": ["y"],
            "z": ["z"],
        },
        "N": dict.fromkeys(["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["D", "G"]),
        "G": {
            **dict.fromkeys(["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["D", "G"]),
            **dict.fromkeys(["0"], ["0", "G"]),
            **dict.fromkeys(['+', '-', '*', '>', ')', ';', 'd'], ""),
        },
        "D": {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"],
            "4": ["4"],
            "5": ["5"],
            "6": ["6"],
            "7": ["7"],
            "8": ["8"],
            "9": ["9"],
        }
    }

terminals = list("0123456789xyzwhiledots();+-*>=")