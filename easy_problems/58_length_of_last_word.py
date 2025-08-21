def length_of_last_word(s: str) -> int:
    word = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " " and word > 0:
            return word
        if s[i] != " ":
            word += 1
    return word
