
def name_to_formula(name):
    formula = ""
    i = 0
    while i < len(name):
        count = 1
        while i + 1 < len(name) and name[i] == name[i + 1]:
            count += 1
            i += 1
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        list_letters = [str(i) for i in letters]
        for j in list_letters:
            if name[i] == j:
                formula += j
        if count > 1:
            formula += str(count)
        i += 1
    return formula


print(name_to_formula("CHHHCOOH"))  # Output: "H2CO2H2"
