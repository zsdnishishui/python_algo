'''
练习递归，重点体会递和归
'''


def recur_sum(n: int):
    '''普通递归'''
    # 触底反弹：基本条件
    if n == 1:
        return 1
    # 调用自己
    # tmp 是归的部分
    tmp = n + recur_sum(n - 1)
    return tmp


def recur_sum_tail(n: int, s=0):
    '''尾递归'''
    # 触底反弹：基本条件
    if n == 1:
        return s + n
    # 最后调用自己
    return recur_sum_tail(n - 1, s + n)


def n_cheng(n: int):
    '''计算n!'''
    if n == 1:
        return 1
    tmp = n * n_cheng(n - 1)
    return tmp


def fei(n: int):
    '''菲波那耶数列'''
    if n == 1 or n == 2:
        return 1
    tmp1 = fei(n - 1)
    tmp2 = fei(n - 2)
    return tmp1 + tmp2


if __name__ == '__main__':
    sum = recur_sum(10)
    print(sum)
    tail = recur_sum_tail(10)
    print(tail)
    n = n_cheng(10)
    print(n)
    num = fei(10)
    print(num)
