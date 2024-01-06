from my_circular_queue import CircularQueue
from my_naive_queue import QueueError

class PriorityQueue:
    "Multiple circular queues"
    def __init__(self, *items, **kwargs):
        self.__queues = {}
        self.__type: type = kwargs.get("type") or type(items[0][0])
        kwargs["type"] = self.__type 
        # queues must be declared with a type or with items, we need to set the
        # type as a keyword arg so that we can declare them empty
        for level in kwargs.get("levels") or [i for i in range(5)]:
            self.__queues[level] = CircularQueue(**kwargs)

        for (item, level) in items:
            self.__queues[level].enqueue(item)

        self.__len  = len(items)
        self.__size = kwargs.get("size") or len(items)

    def is_full(self):
        return self.__len == self.__size

    def is_empty(self):
        return self.__len == 0
    
    def enqueue(self, item, level):
        if self.is_full():
            raise QueueError("Queue full!")

        if self.__queues.get(level) is None:
            raise QueueError(f"{level} is not a priority level")

        try:
            self.__queues[level].enqueue(item)
        except QueueError as e:
            raise QueueError(e)

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue empty!")

        for queue in self.__queues.values():
            if not queue.is_empty():
                return queue.dequeue()
    
    def __repr__(self):
        r = ""
        for q in self.__queues.values():
            s = repr(q)[6:len(repr(q))-1]
            if s:
                r += s+", "

        return f"Queue[{r[:-2]}]"

    def __len__(self):
        "Called by len() & queue will be falsey with length 0"
        return self.__len

if __name__ == "__main__":
    q = PriorityQueue((1, 1), (2, 0), (3, 2), size=5)
    print("q = PriorityQueue((1, 1), (2, 0), (3, 2), size=5)")
    print("--------------------------------")

    while True:
        print(f"\n{q}")
        item = input(">> ")
        if item == "-1":
            try:
                q.dequeue()
            except QueueError as e:
                print(e)
        else:
            try:
                (item, level) = (int(item.split()[0]), int(item.split()[1]))
            except Exception as e:
                print(e)
            else:
                try:
                    q.enqueue(item, level)
                except QueueError as e:
                    print(e)
                




