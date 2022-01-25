"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""

"""
Sol: Count the frequencies of all characters.
create a list frequesncies.
Iterate over the charCount.values()
if the value is not in frequency list, then add it to freq List
else, decrement the val till the val is not in freq list. 
"""

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        charCount = Counter(s)
        frequency = []
        result = 0
        for val in charCount.values():
            if val not in frequency:
                frequency.append(val)
            else:
                while val > 0:
                    if val not in frequency:
                        frequency.append(val)
                        break
                    else:
                        val -= 1
                        result += 1
        return result


cl = Solution()
ans = cl.minDeletions("aaabbbcc")
print(ans)
