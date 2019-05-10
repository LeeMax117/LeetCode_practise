class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k :
            return 0
        letter_dict = {}
        for index,i in enumerate(s):
            if i not in letter_dict:
                letter_dict[i] = [index]
            else:
                letter_dict[i].append(index)

        seperate = []
        count = 0
        for letter in letter_dict:
            if len(letter_dict[letter]) < k:
                count += 1
                for i in letter_dict[letter]:
                    seperate.append(i)
        if count == len(letter_dict):
            return 0

        if seperate == []:
            return len(s)
        else:
            if len(s) - seperate[-1] <= k:
                longest = self.longestSubstring(s[:seperate[0]], k)
            else:
                longest = max(self.longestSubstring(s[:seperate[0]],k), self.longestSubstring(s[seperate[-1] + 1:],k))
            for index in range(1,len(seperate)):
                longest = max(longest,self.longestSubstring(s[seperate[index-1]:seperate[index]],k))
            return longest

if __name__ == '__main__':
    a = Solution()
    print(a.longestSubstring("bbaaacbd",3))