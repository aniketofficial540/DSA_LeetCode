class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0

        dictRoman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for a, b in zip(s, s[1:]):

            if dictRoman[a] >= dictRoman[b]:
                count += dictRoman[a]
            else:
                count -= dictRoman[a]
        return count + dictRoman[s[-1]]