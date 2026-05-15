class Solution:
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:

            # Sort ký tự để làm key
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())