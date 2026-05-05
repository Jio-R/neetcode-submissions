class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "█"

        output = ""

        for i in strs:
            output += i+'░'
        
        return output[:-1]

    def decode(self, s: str) -> List[str]:
        
        
        if s == "█":
            return []

        output = [""]

        for i in s:
            if i == '░':
                output.append('')
                continue
            output[-1] += i
        
        return output