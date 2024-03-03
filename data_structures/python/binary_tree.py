class Node:
    def __init__(self, *nums):
        self.__n, *nums = nums
        self.__l = None
        self.__r = None

        for n in nums:
            self.append(n)

    def append(self, n):
        if n <= self.__n:
            if self.__l == None: 
                self.__l = Node(n)
            else:
                self.__l.append(n)
        else:
            if self.__r == None: 
                self.__r = Node(n)
            else:
                self.__r.append(n)

    def pre_order(self):
        order = []
        order.append(self.__n)
        if self.__l != None:
            order += self.__l.pre_order()
        if self.__r != None:
            order += self.__r.pre_order()
        return order

    def in_order(self):
        order = []
        if self.__l != None:
            order += self.__l.in_order()
        order.append(self.__n)
        if self.__r != None:
            order += self.__r.in_order()
        return order

    def post_order(self):
        order = []
        if self.__l != None:
            order += self.__l.post_order()
        if self.__r != None:
            order += self.__r.post_order()
        order.append(self.__n)
        return order

    def __repr__(self):
        return f"{self.__n}({self.__l or '_'} {self.__r or '_'})"

if __name__ == '__main__':
    t = Node(40, 30, 50, 25, 35, 45, 60, 15, 28, 55, 70);
    print(t)
    print(f"PRE:  {t.pre_order()}")
    print(f"IN:   {t.in_order()}")
    print(f"POST: {t.post_order()}")

