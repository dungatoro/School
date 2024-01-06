from my_array import Array

class NaiveQueue:
    def __init__(self, *items, **kwargs):
        self.__queue = Array(*items, **kwargs)
        self.__head  = 0
        self.__tail  = len(items)

    def is_full(self):
        return self.__tail == len(self.__queue)

    def is_empty(self):
        return self.__head == self.__tail

    def enqueue(self, item):
        "Add to the back"
        if self.is_full():
            raise QueueError("Queue full!")

        self.__queue[self.__tail] = item
        self.__tail += 1

    def dequeue(self):
        "Remove from the front"
        if self.is_empty():
            raise QueueError("Queue empty!")

        item = self.__queue[self.__head]
        self.__head += 1
        return item

    def __repr__(self):
        "Called by print()"
        return f"Queue{[self.__queue[i] for i in range(self.__head, self.__tail)]}"

    def __len__(self):
        "Called by len() & queue will be falsey with length 0"
        return self.__tail - self.__head

class QueueError(Exception):
    " This lets us match a queue specific error `except QueueError: ...` "
    pass

if __name__ == "__main__":
    q = NaiveQueue(2, 3, 4, size=5)
    print("q = NaiveQueue(2, 3, 4, size=5)")
    print("-------------------------------")

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

