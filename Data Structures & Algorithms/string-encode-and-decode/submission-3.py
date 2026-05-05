class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "█"

        output = '░'.join(strs)
        
        return output

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