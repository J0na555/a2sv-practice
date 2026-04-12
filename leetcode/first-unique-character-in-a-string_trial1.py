class Solution:
    def firstUniqChar(self, s: str) -> int:
       counter = Counter(s) 

       for idx, count in enumerate(s):

