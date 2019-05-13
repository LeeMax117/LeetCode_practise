class Solution:
    def expressiveWords(self, S, words):
        cnt = 0
        for word in words:
            index = 0
            count = 0
            tmp = ''
            index_stop = False
            for i in S:
                try:
                    if i == word[index]:
                        if tmp != i:
                            if index_stop:
                                if count < 2:
                                    break
                                else:
                                    index_stop = False
                             count = 0
                        else:
                            count += 1
                        tmp = i
                        index += 1
                    elif i == tmp:
                        count += 1
                        index_stop = True
                    else:
                        break

                except IndexError:
                    if i == tmp and i == word[-1]:
                        count += 1
                        index_stop = True
                    else:
                        break
            else:
                if index == len(word):
                    if not index_stop or count >= 2:
                        cnt += 1
        return cnt

if __name__ == '__main__':
    a = Solution()
    print(a.expressiveWords("dddiiiinnssssssoooo",
["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
))

