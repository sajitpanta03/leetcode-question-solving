
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            # Step 1: Create frequency hashmap
            frequency = {}

            # Step 2: Count each character
            for char in word:

                if char not in frequency:
                    frequency[char] = 1
                else:
                    frequency[char] += 1

            # Step 3: Sort character-frequency pairs
            key = tuple(sorted(frequency.items()))

            # Step 4: Check if the key exists
            if key not in groups:
                groups[key] = []

            # Step 5: Add word to its group
            groups[key].append(word)

        # Step 6: Return grouped words
        return list(groups.values())

