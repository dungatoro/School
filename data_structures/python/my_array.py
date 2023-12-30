class Array:
    def __init__(self, *items, **kwargs):
        """ Generate an array with optional items, and size """
        self.__type: type = kwargs.get("type") or type(items[0])
        if not all( isinstance(i, self.__type) for i in items):
            raise ArrayError(f"Expected type {self.__type}, found {type(item)}.")

        self.__size: int = kwargs.get("size") or len(items)
        if self.__size < len(items):
            raise ArrayError(f"Array created with more items than expected")

        # Pad array with `None` if 'size' > len(items)
        self.__arr = list(items) + [None]*(self.__size-len(items))

    def __getitem__(self, idx):
        return self.__arr[idx]

    def __setitem__(self, idx, item):
        if not isinstance(item, self.__type):
            raise ArrayError(f"Tried to assign item of type {type(item)} to array of {self.__type}")

        self.__arr[idx] = item

    def __iter__(self):
        """ Lets us use `for i in arr: ...` """
        yield from self.__arr

    def __repr__(self) -> str:
        """ Called by print() """
        return f"Array{self.__arr}"

    def __len__(self) -> int:
        """ Called by len() """
        return self.__size

class ArrayError(Exception):
    pass

if __name__ == "__main__":
    arr = Array(1, 2, 3, type=int, size=10)
    print("arr = Array(1, 2, 3, type=int, size=10)")
    print("---------------------------------------")

    while True:
        print(arr)
        try:
            item = int(input("Item  >> "))
            idx  = int(input("Index >> "))
        except ValueError as e: 
            print(e)
        else:
            try:
                arr[idx] = item
            except ArrayError as e: 
                print(e)





