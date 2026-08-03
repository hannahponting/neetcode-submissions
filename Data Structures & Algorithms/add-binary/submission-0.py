class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        a = a[::-1]
        b = b[::-1]
        carry = 0

        for i in range(max(len(a), len(b))):
            a_char = ord(a[i]) - ord('0') if i < len(a) else 0
            b_char = ord(b[i]) - ord('0') if i < len(b) else 0

            total = a_char + b_char + carry
            res = f'{total % 2}' + res
            carry = total // 2

        if carry:
            res = '1' + res

        return res


            