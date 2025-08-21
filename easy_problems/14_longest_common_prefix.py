def longest_common_prefix(strs: list[str]):
    if not strs:
        return ""
    min_word = min(strs, key=len)
    cur_prefix = ""
    for i, letter in enumerate(min_word):
        if not all(word[i] == letter for word in strs):
            return cur_prefix
        cur_prefix += letter
    return cur_prefix


# s = ["flower", "flow", "flight"]
s = ["dog", "racecar", "car"]
print(longest_common_prefix(s))


# TODO другое решение

# def longestCommonPrefix(self, strs: List[str]) -> str:
#     if not strs:
#         return ""
#
#     prefix = strs[0]
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix
