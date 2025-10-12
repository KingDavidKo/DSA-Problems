class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        temp = ""
        for i in logs:
            if i[-1].isdigit():
                digit_log.append(i)
            else:
                letter_log.append(i)
        
        letter_log.sort(key = lambda log: log.split(" ", 1)[0])
        letter_log.sort(key = lambda log: log.split(" ", 1)[1])
        return letter_log + digit_log
            

        