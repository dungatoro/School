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

    def __repr__(self):
        return f"{self.__n}({self.__l or '_'} {self.__r or '_'})"


if __name__ == '__main__':
    t = Node(12, 9, 7, 10, -4, 4, 62);
    print(t)

