


#while the value from first word[i] is == to the value of the current word[i], check next word
#if value from first word does NOT equal the value of current word[i], then return prefix -1 letter


def longestCommonPrefix(List):
    prefix =''
    for i in range(len(List[0])):
        for x in List[1:]: #for every other word
            if List[0][i] !=x[i]:
                if i == 0:
                    return ''
                else:
                    return prefix
        prefix += List[0][i]
    return prefix





print(longestCommonPrefix(["dog","racecar","car"]))
