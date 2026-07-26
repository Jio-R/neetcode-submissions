class Solution:
    def isValid(self, s: str) -> bool:
        d = dict()

        d['('] = d['{'] = d['['] = 0
        left = set(['(', '{', '['])
        right = set([')', '}', ']'])

        print(f"s: {s}, d: {d}")

        for c in s:
            print(c)
            if c in left:
                d[c] -= 1
                print(d)
                continue
            match c:
                case ')':
                    d['('] += 1
                case ']':
                    d['['] += 1
                case '}':
                    d['{'] += 1
            print(d)
            
        if d['('] == d['{'] == d['['] == 0:
            return True
        return False