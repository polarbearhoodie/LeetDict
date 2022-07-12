
def possible_strings(str_in):
    ref = {2: "abc",
           3: "def",
           4: "ghi",
           5: "jkl",
           6: "mno",
           7: "pqrs",
           8: "tuv",
           9: "wxyz"}

    combos = []
    for char in ref[int(str_in[0])]:
        combos.append(char)

    for char in str_in[1:]:
        key = int(char)
        for i in range(len(combos)): # len(combos) needs to avoid mutation
            s = combos.pop(0)
            related_chars = ref[key]
            for char_2 in related_chars:
                combos.append(s + char_2)

    return combos
