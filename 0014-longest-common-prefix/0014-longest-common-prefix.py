class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        first = strs[0]
        matched = []

        for i in range(len(first)):
            char = first[i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return "".join(matched)

            matched.append(char)
        
        return "".join(matched)