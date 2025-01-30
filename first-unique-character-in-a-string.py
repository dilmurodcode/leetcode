class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = {}

        for i in s:
            if i in result.keys():
                result[i] = result[i] + 1
            else:
                result[i] = 1

        for j in range(len(s)):
            if result[s[j]] == 1:
                return j

        return -1

a = Solution()
print(a.firstUniqChar('leetcode'))