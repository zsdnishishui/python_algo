import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from untils import TreeNode, print_tree


def guang_du(node: TreeNode):
    '''广度优先搜索需要*借助队列*实现'''
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def pre_traverse(node: TreeNode):
    '''深度优先搜索的前序遍历'''
    if node == None:
        return
    print(node.val)
    pre_traverse(node.left)  # 深入递归
    pre_traverse(node.right)  # 归的部分


def mid_traverse(node: TreeNode):
    '''深度优先搜索的前序遍历'''
    if node == None:
        return

    mid_traverse(node.left)
    print(node.val)
    mid_traverse(node.right)


def after_traverse(node: TreeNode):
    '''深度优先搜索的前序遍历'''
    if node == None:
        return

    after_traverse(node.left)
    after_traverse(node.right)
    print(node.val)


if __name__ == '__main__':
    root = TreeNode(1)
    left1 = TreeNode(2)
    right1 = TreeNode(3)
    left2 = TreeNode(4)
    left3 = TreeNode(5)
    # left4 = TreeNode(6)
    root.left = left1
    root.right = right1
    left1.left = left2
    left1.right = left3
    # left2.right = left4
    print_tree(root)
    print("-----前序-----")
    pre_traverse(root)
    print("------中序-----")
    mid_traverse(root)
    print("-----后序----")
    after_traverse(root)
    print("-----广度优先搜索----")
    guang_du(root)
