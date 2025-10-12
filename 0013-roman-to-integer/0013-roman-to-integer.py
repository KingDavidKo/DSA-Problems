class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        i = 0

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        while i < len(s):
            if len(s) - i >= 2:
                frag = s[i] + s[i+1]
                if frag == "IV":
                    total += 4
                    i += 2
                elif frag == "IX":
                    total += 9
                    i += 2
                elif frag == "XL":
                    total += 40
                    i += 2
                elif frag == "XC":
                    total += 90
                    i += 2
                elif frag == "CD":
                    total += 400
                    i += 2
                elif frag == "CM":
                    total += 900
                    i += 2
                else:
                    total += values[s[i]]
                    i += 1
            else:
                total += values[s[i]]
                i += 1
        return total

                
        