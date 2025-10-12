class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        characters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        for i in range(len(tasks)):
            characters[ord(tasks[i]) - ord('A')] += 1
        
        max_freq = max(characters)


        max_count = 0
        for i in range(26):
            if characters[i] == max_freq:
                max_count += 1
            
        return max(len(tasks), (n+1) * (max_freq - 1) + max_count)
            
        



        