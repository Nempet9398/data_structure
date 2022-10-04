# Stack => Last in First - out (LIFO)
# Queue => First - In First - OUT (FIFO)


# 스택

# push (삽입), pop (삭제)




## 클래스 버전

class Stack:

    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0

    def size(self): return len(self.top)

    def clear(self) : self.top = []

    def push(self,item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.Empty():
            return self.top[-1]



## 1번문제 - 다항식표현

def printpoly(a, n):
    origin = "P(x) = "

    for i in range(len(n)):
        a_number = a[i]
        n_number = n[i]

        if (n_number >=0):
            origin += "+"

        origin += str(a_number) + "x^" + str(n_number) + " "

    return origin


def calpoly(a, n):

    value = 0

    for i in range(len(n)):
        a_number = a[i]
        n_number = n[i]
        value += a_number * (xvalue ** n_number)

    return value

# 계수 a 설정
# a_list = [3,4,2]
#
# # 계수 b
# n_list = [5,2,1]
#
# print(printpoly(a_list,n_list))
# xvalue = 2
# print('결과는 다음과 같습니다. ',calpoly(a_list,n_list))


#2번
size = 5
stack = [None,None,None,None]
top = -1

## 함수버전


def isStackFull():
    global size , stack , top
    if (top >= size-1):
        return True

    else:
        return False


def isStackEmpty():
    global size, stack, top

    if (top== -1):
        return True

    else:
        return False

def push(data):
    global size, stack, top

    if (isStackFull()):
        print('꽉 찼습니다')
        return

    top += 1
    stack[top] = data


def pop():
    global size, stack,top
    if (isStackEmpty()):
        print('스택이 비었습니다.')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global size, stack, top

    if (isStackEmpty()):
        print('비었습니다.')
        return None

    return stack[top]

def printreverse(string_word):


    ## string_word 크기의 스택을 생성
    stack = [None for _ in range(len(string_word))]
    size = len(string_word)
    top = -1

    def push(data):
        global size, stack, top

        if (isStackFull()):
            print('꽉 찼습니다')
            return

    def isStackFull():
        global size , stack , top
        if (top >= size-1):
            return True

        else:
            return False
    top += 1
    stack[top] = data
    ## 각 단어를 push 하여 stack에 저장
    for i in string_word:
        push(i)

    for _ in range(len(stack)):
        word = pop()
        print(word, end='')


printreverse('hello world')
