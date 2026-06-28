class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        anagram_map=defaultdict(list)
        for i,string in enumerate(strs):
            anagram_map[frozenset(Counter(string).items())].append(i)
        for _,grp in anagram_map.items():
            out.append([strs[i] for i in grp])
        return out