## 원형 연결리스트 생성

class Node():
    def __init__(self):
        self.data = None
        self.link = None



def printNodes(start):
    current = start
    if current.link ==None:
        return

    print(current.data, end=' ')
    print()
    while current.link != start :
        current = current.link
        print(current.data, end=' ')

        print()

memory = []

head, current, pre = None, None, None
dataArray=['다현','정연','쯔위','사나','지효']

if __name__ == '__main__':

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

printNodes(head)

print('-'*20)

## 노드 삽입
#
def insertNode(findData, insertData):
    global memory , head, current, pre

    ## 맨 앞에 들어갈 때
    if head.data = findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return


    current = head
    while current.link != head:
        pre = current
        current = current.link
        ## 중간에 들어갈 때
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = curnet
            pre.link = node
            return

    ## 마지막
    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

## 노드삭제함수

def deleteNode(deleteData):
    global memory, head, current, pre:

    if head.data = deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link

        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

##과제 makecircularLinkedList(namephone) 만들기
## current link 가 head인것을 확인해야함
