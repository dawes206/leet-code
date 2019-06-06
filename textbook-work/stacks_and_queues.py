class Stack(list):
    def __init__(self, size):
        self.top = 0
        for i in [None]*size:
            self.append(i)

    def push(self,num):
        if self[self.top]==None:
            self[self.top] = num
        else:
            self.top = self.top + 1
            self[self.top] = num

    def pop(self):
        if len(self) == 0:
            print('underflow')
        else:
            popped = self[self.top]
            self.top -= 1
            return popped


# test = Stack(5)
# test.push(3)
# test.push(4)
# test.push(3)
# print('test after pushing', test)
# r= test.pop()
# print('pointer and val after pop: ',test.top, test[test.top])
# print('value of popped: ', r)
# r2 = test.pop()
# print('pointer and val after pop2: ',test.top, test[test.top])
# print('value of popped2: ', r2)



class Queue(list):
    def __init__(self,size):
        for i in [None]*size:
            self.append(i)
        self.head = 0
        self.tail = 0

    def enqueue(self,num):
        # print('old tail: ', self[self.tail])
        self[self.tail]=num
        self.tail += 1
        if self.tail == len(self):
            self.tail = 0
        # print('new tail -1 : ', self[self.tail -1 ])

    def dequeue(self):
        x = self[self.head]
        self.head += 1
        if self.head == len(self) + 1:
            self.head = 0
        return x



# test= Queue(5)
# print(test)
# test.enqueue(3)
# test.enqueue(5)
# test.enqueue(6)
# print(test)
# d1 = test.dequeue()
# print('d1: ', d1)
# print('head', test[test.head])
# d2 = test.dequeue()
# print('d2: ', d2)
# print(test)
