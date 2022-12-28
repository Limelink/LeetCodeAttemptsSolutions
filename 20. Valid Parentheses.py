"""20. Valid Parentheses"""

class Solution:
    def isValid(self, s: str) -> bool:
        signs = list(s)
        print(s)

        mod_s = s
        for i in range(len(mod_s)):
            if "{}" in s:
                s = s.replace("{}", "")
                print(s)

            if "[]" in s:
                s = s.replace("[]", "")
                print(s)

            if "()" in s:
                s = s.replace("()", "")
                print(s)

            if s == "":
                return True
            else:
                return False

solution = Solution()
solution.isValid("()[]{}")