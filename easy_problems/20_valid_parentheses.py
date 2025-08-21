def is_valid(s: str) -> bool:
    parentheses = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    current_open_parentheses = []
    for symbol in s:
        if symbol in parentheses:
            current_open_parentheses.append(symbol)
        elif symbol in parentheses.values():
            if not current_open_parentheses:
                return False
            if parentheses[current_open_parentheses.pop()] != symbol:
                return False
    if current_open_parentheses:
        return False
    return True


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([])"))
