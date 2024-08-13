"""
数组
"""
class Array:
    def __init__(self,size):
        self.array = [None]*size
        self.size = size


    def get_size(self):
        return self.size

    def get_index(self,value):
        pass
    def insert(self,index,value):
        pass

    def delete(self,index):
        pass

    def get_value(self,index):
        pass


if __name__ == '__main__':
    # 初始化
    a = Array(10)
    # 添加
    # 删除
    # 查找
    # 遍历
    print(a.array)