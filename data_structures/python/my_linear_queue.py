from my_naive_queue import QueueError
from my_array import Array

class LinearQueue:
    def __init__(self, *items, **kwargs):
        self.__queue = Array(*items, **kwargs)
        self.__head  = 0
        self.__tail  = len(items)

    def is_full(self):
        return self.__tail == len(self.__queue)

    def is_empty(self):
        return self.__head == self.__tail

    def enqueue(self, item):
        """Add to the back"""
        if self.is_full():
            raise QueueError("Queue full!")

        self.__queue[self.__tail] = item
        self.__tail += 1

    def dequeue(self):
        """Shuffle items after dequeue"""
        if self.is_empty():
            raise QueueError("Queue empty!")

        item = self.__queue[self.__head]
        for i in range(1, self.__tail):
            self.__queue[i-1] = self.__queue[i]

        self.__tail -= 1

        return item

    def __repr__(self):
        """Called by print()"""
        return f"Queue{[self.__queue[i] for i in range(self.__head, self.__tail)]}"

    def __len__(self):
        """Called by len() & queue will be falsey with length 0"""
        return self.__tail - self.__head

if __name__ == "__main__":
    q = LinearQueue(1, 2, 3, size=5)
    print("q = LinearQueue(1, 2, 3, size=5)")
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

