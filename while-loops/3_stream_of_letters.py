n_found = False
o_found = False
c_found = False

word = ""
result = ""

while True:
    symbol = input()

    if symbol == "End":
        break

    if not symbol.isalpha() or not symbol.isascii():
        continue

    if symbol == "n":
        if not n_found:
            n_found = True
        else:
            word += symbol
    elif symbol == "o":
        if not o_found:
            o_found = True
        else:
            word += symbol
    elif symbol == "c":
        if not c_found:
            c_found = True
        else:
            word += symbol
    else:
        word += symbol

    if n_found and o_found and c_found:
        result += word + " "
        word = ""
        n_found = False
        o_found = False
        c_found = False

print(result)