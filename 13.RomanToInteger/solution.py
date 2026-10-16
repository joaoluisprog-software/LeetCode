class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictio ={ "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                    "IV": 4,
                    "IX": 9,
                    "XL": 40,
                    "XC": 90,
                    "CD": 400,
                    "CM": 900 }
        sum, i, string_length = 0, 0, len(s)
        while i < string_length:
            if i + 1 < string_length and (s[i] + s[i + 1]) in dictio:
                sum += dictio[s[i] + s[i + 1]]
                i += 2
            else:     
                sum += dictio[s[i]]
                i += 1 
        
        return sum