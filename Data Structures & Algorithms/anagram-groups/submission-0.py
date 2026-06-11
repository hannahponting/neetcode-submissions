class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            sorted_word = str(sorted(i))
            if result.get(sorted_word):
                result[sorted_word].append(i)
            else: 
                result[sorted_word] = [i]
        final_list = []
        for key in result.keys():
            final_list.append(result[key])
        return final_list
            