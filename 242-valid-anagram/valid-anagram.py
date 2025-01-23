class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # # HashArray approach
        # Time : O(N)
        # Space : O(1)
        # counter = [0] * 26

        # for ch in s:
        #     counter[ord(ch) - ord('a')] += 1

        # for ch in t:
        #     counter[ord(ch) - ord('a')] -= 1
        
        # for n in counter:
        #     if n != 0:
        #         return False

        # return True

        # inBuilt Counter approach
        
        return Counter(s) == Counter(t)

        # HashTable approach
        sMap = {}
        tMap = {}
        
        for ch in s:
            if ch in sMap:
                sMap[ch] += 1
            else:
                sMap[ch] = 1
        
        for ch in t:
            if ch in tMap:
                tMap[ch] += 1
            else:
                tMap[ch] = 1

        for ch in tMap:
            if ch not in sMap:
                return False
            if sMap[ch] != tMap[ch]:
                return False

        return True