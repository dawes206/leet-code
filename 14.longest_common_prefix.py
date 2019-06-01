


#while the value from first word[i] is == to the value of the current word[i], check next word
#if value from first word does NOT equal the value of current word[i], then return prefix -1 letter

class Solution():
    # def longestCommonPrefix(self, List):
    #     prefix = ''
    #     if len(List) == 0:
    #         return ""
    #     firstWordLen = len(List[0])
    #     for letterNum in range(firstWordLen):
    #         for word in List[1:]: #for every other word
    #             if List[0][letterNum] !=word[letterNum]:
    #                 if letterNum == 0:
    #                     return ''
    #                 else:
    #                     return prefix
    #         prefix += List[0][letterNum]
    #     return prefix

    def longestCommonPrefix(self,List):
        prefix = ''
        #empty string condition
        if len(List)==0:
            return ''
        letterCounter = 1
        List.sort()
        seedWord = List[0]
        prefix = ''
        while letterCounter<=len(seedWord):
            for word in List:
                if word[letterCounter-1] != seedWord[letterCounter-1]:
                    if letterCounter == 1:
                        return ''
                    else:
                        return prefix
            prefix += seedWord[letterCounter-1]
            letterCounter += 1
        return prefix



test = Solution()

print(test.longestCommonPrefix(['flow','reace']))
