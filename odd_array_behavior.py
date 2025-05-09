def addToArray(arrayToModify):
    arrayToModify += 5

    # newNum = arrayToModify
    # idBefore = id(newNum)
    # newNum += 1
    # idAfter = id(newNum)
    # if idBefore == idAfter:
    #     print('ints match')
    # else:
    #     print('ints do not match')

    return 'return value'

test = 0
addToArray(test)
print(test) #prints 0




def addToArray(arrayToModify):
    arrayToModify[0] = 5

    # newArray = arrayToModify
    # idBefore = id(newArray)
    # newArray[0] += 1
    # idAfter = id(newArray)
    # if idBefore == idAfter:
    #     print('arrays match')
    # else:
    #     print('arrays do not match')

    return 'return value'

test = [0]
addToArray(test)
print(test) #prints [5]

#It's because lists are mutable. This means that test2 = test; test2 += [1]; test will also be changed. Test2 REFERENCES the same memory space that test references.
#Int's are immutable. It means when you assign
#Actually, I think it's really because += operator changes the list in place. If you do list2= list +[val], list will actually stay the same, and a new memory space will be made for l2.  BUt, the reason that the value of test persists through the function is because it's always pointing at the same memory space. Because lists are mutable, when you perform the += operator on the list, it keeps the same reference to that space in memory. Int's do not. They are immutable. If you modify an int, the new variable will point to a different place in memory.
