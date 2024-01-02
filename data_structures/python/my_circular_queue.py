from my_naive_queue import QueueError
from my_array import Array

class CircularQueue:
    def __init__(self, *items, **kwargs):
        self.__queue = Array(*items, size=kwargs.get("size") or len(items))
        self.__head  = 0
        self.__tail  = len(items)

    def enqueue(self, item):
        " "
        if self.__tail == len(self.__queue):
            raise QueueError("Queue full!")

        self.__queue[self.__tail] = item
        self.__tail += 1

    def dequeue(self):
        " "
        if self.__head == self.__tail:
            raise QueueError("Queue empty!")

        item = self.__queue[self.__head]
        for i in range(1, self.__tail):
            self.__queue[i-1] = self.__queue[i]

        self.__tail -= 1

        return item

    def __repr__(self):
        " Called by print() "
        # return f"Queue{[self.__queue[i] for i in range(self.__head, self.__tail)]}"

    def __len__(self):
        " Called by len() "
        # return self.__tail - self.__head

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
