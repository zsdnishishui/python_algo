"""
基于数组实现的链式寻址
"""


class ChainHashMap:

    def __init__(self):
        self.capacity = 16  # 容量
        # 负载因子：
        self.load_factor = 0.75
        self.size = 0
        self.extended_size = 2

    def get_size(self):
        return self.size

    def hash_func(self):
        pass

    def put(self, key, value):
        pass

    def remove(self, key):
        pass

    def extend(self):
        pass

    def entry_set(self):
        """获取所有键值对"""
        pass

    def get_keys(self):
        """获取所有键"""
        pass

    def get_values(self):
        """获取所有值"""
        pass

    def print(self):
        """打印hashmap"""
        pass
