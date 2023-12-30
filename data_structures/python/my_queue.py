from my_array import Array

class NaiveQueue:
    def __init__(self, *items, **kwargs):
        self.__queue = Array(*items, size=kwargs.get("size") or len(items))
        self.__head  = 0
        self.__tail  = len(items)

    def enqueue(self, item):
        if self.__tail == len(self.__queue):
            raise Exception("Queue full!")

        self.__queue[self.__tail] = item
        self.__tail += 1

    def dequeue(self):
        if self.__head == self.__tail:
            raise Exception("Queue empty!")

        item = self.__queue[self.__head]
        self.__head += 1
        return item

if __name__ == "__main__":
    q = NaiveQueue(2, 3, 4, size=5)




