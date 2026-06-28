# hash map, counter and frozen set
# O(m*n) time and O(n) space
class SolutionV1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for string in strs:
            anagram_map[frozenset(Counter(string).items())].append(string)
        return list(anagram_map.values())


# canonical solution: counting array
# O(m*n) time and O(n) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for string in strs:
            count_array = [0] * 26
            for char in string:
                count_array[ord(char) - ord("a")] += 1
            anagram_map[tuple(count_array)].append(string)
        return list(anagram_map.values())
