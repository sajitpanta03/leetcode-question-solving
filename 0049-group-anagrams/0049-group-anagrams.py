from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            frequency = {}

            # Count characters and store their indexes
            for index, char in enumerate(word):
                if char not in frequency:
                    frequency[char] = []

                frequency[char].append(index)

            # Create a comparable key
            key = tuple(sorted(
                (char, len(indexes))
                for char, indexes in frequency.items()
            ))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        result = list(groups.values())

        return result