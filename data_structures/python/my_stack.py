from my_array import Array

class Stack:
    def __init__(self, *items, **kwargs):
        self.__stack = Array(*items, size=kwargs.get("size") or len(items))
        self.__tos   = len(items)
        
    def push(self, item):
        """ Push an item to the top of stack if not full """
        if self.__tos == len(self.__stack):
            raise Exception(f"Stack full!")

        self.__stack[self.__tos] = item
        self.__tos += 1

    def pop(self):
        """ Pop an item from the top of stack if not empty """
        if self.__tos == 0:
            raise Exception(f"Stack empty!")

        self.__tos -= 1
        return self.__stack[self.__tos]
    
    def __iter__(self):
        """ Pops each item in sequence """
        while self.__tos != 0:
            yield self.pop()

    def __repr__(self) -> str:
        """ Called by print() """
        msg = [self.__stack[i] for i in range(self.__tos)]
        return f"Stack{msg}"

    def __len__(self) -> int:
        """ Called by len() """
        return self.__tos


if __name__ == "__main__":
    stack = Stack(1, 2, 3, size=5)

    print(stack)

    for item in stack:
        print(item)

    print(stack)




