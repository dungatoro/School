from my_naive_queue import QueueError
from my_array import Array

class CircularQueue:
    def __init__(self, *items, **kwargs):
        kwargs["size"] = (kwargs.get("size") or len(items)) +1
        self.__queue = Array(*items, **kwargs)
        self.__head  = 0
        self.__tail  = len(items)

    def is_full(self):
        return self.__tail == (self.__head-1) % len(self.__queue)

    def is_empty(self):
        return self.__head == self.__tail

    def enqueue(self, item):
        """Add to the back"""
        if self.is_full():
            raise QueueError("Queue full!")

        self.__queue[self.__tail] = item
        self.__tail = (self.__tail + 1) % len(self.__queue)

    def dequeue(self):
        """Remove from the front"""
        if self.is_empty():
            raise QueueError("Queue empty!")

        item = self.__queue[self.__head]
        self.__head = (self.__head+1) % len(self.__queue)
        return item

    def __repr__(self):
        """Called by print()"""
        l = []
        i = self.__head
        while i != self.__tail:
            l.append(self.__queue[i])
            i = (i+1) % len(self.__queue)

        return f"Queue{l}"

    def __len__(self):
        """Called by len() & queue will be falsey with length 0"""
        return self.__tail - self.__head

if __name__ == "__main__":
    q = CircularQueue(1, 2, 3, size=5)
    print("q = CircularQueue(1, 2, 3, size=5)")
    print("--------------------------------")

    while True:
        print(f"\n{q}")
        try:
            item = int(input(">> "))
        except ValueError as e:
            print(e)
        else:
            if item == -1:
                try:
                    q.dequeue()
                except QueueError as e:
                    print(e)
            else:
                try:
                    q.enqueue(item)
                except QueueError as e:
                    print(e)
