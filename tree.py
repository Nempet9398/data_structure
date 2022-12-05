## Tree 구현

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right =None

node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '다현'
node4.right = node6

node7 = TreeNode()
node7.data = '선미'
node3.left = node7

node8 = TreeNode()
node8.data = '사나'
node7.right = node8


## 이진트리 순회 구현

def preorder(node):
    if node ==None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node==None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)

def postorder(node):
    if node==None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')

# print('전위 순회 : ',end='')
# preorder(node1)
# print('끝')
#
# print('전위 순회 : ',end='')
# inorder(node1)
# print('끝')
#
# print('후위 순회 : ',end='')
# postorder(node1)
# print('끝')

## 노드 개수 구하기
def count_node(n):
    if n in None :
        return 0

    else:
        return 1 + count_node(left) + count_node(right)

def count_leaf(n):
    if n in None:
        return 0
    else n.left is None and n.right is None:
        return 1:
    else :
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n in None:
        return 0

    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft +1
    else:
        return hRight + 1
