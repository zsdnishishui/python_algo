"""
普通链表
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_size(node: ListNode):
    pass


def get_index(node: ListNode):
    pass


def insert(nodeBefore: ListNode, nodeAfter: ListNode):
    pass


def append(node: ListNode):
    pass


def delete(node: ListNode):
    pass


def get_value(node: ListNode, index):
    pass


def recursion(l: ListNode):
    if l is None:
        return
    print(l.value)
    recursion(l.next)


if __name__ == '__main__':
    # 初始化
    l = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(4)
    l.next = l2
    l2.next = l3
    # 添加
    # 删除
    # 查找
    # 遍历
    # while l:
    #     print(l.value)
    #     l = l.next
    recursion(l)
