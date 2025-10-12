class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for i in strs:
            
            temp = " ".join(sorted(i))
            if temp not in freq:
                freq[temp] = [i]
            else:
                freq[temp].append(i)
        output = []

        for i in freq:
            output.append(freq[i])
        return output

        

        