# -*- coding: utf-8 -*-

class IntUtil:
    def twice(self, n):
        """ 引数を 2 倍して返す関数
        >>> mine.twice(8)
        16
        >>> mine.twice(1850923)
        3701846
        """
        return n * 2

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs = {'mine': IntUtil()})
