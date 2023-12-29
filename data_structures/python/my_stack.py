from my_array import Array

class Stack:
    def __init__(self, *items, **kwargs):
        self.__stack = Array(*items, size=kwargs.get("size") or len(items))
        self.__tos   = len(items)
        
    def push(self, item):
        if self.__tos == len(self.__stack):
            raise Exception(f"Stack full!")
        else:
            self.__stack[self.__tos] = item
            self.__tos += 1

    def pop(self):
        if self.__tos == 0:
            raise Exception(f"Stack empty!")
        else:
            self.__tos -= 1
            item = self.__stack[self.__tos]
            return item


if __name__ == "__main__":
    stack = Stack(1, 2, 3, size=5)

    print( stack.pop())

    print( stack.push(1))
    print( stack.push(1))
    print( stack.push(1))
    print( stack.push(1))
    print( stack.push(1))
    print( stack.push(1))





