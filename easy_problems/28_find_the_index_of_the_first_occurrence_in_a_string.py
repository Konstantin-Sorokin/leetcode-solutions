def str_str(haystack: str, needle: str) -> int:
    start = 0
    while len(haystack) - start >= len(needle):
        if haystack[start : len(needle)] == needle:
            return start
        start += 1

    return -1


a = str_str(haystack="aaa", needle="aaa")
print(a)
