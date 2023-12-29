class Array:
    def __init__(self, *items, **kwargs):
        """ Generate an array with optional items, and size """

        self.__type: type = kwargs.get("type") or type(items[0])
        if not all( isinstance(i, self.__type) for i in items):
            raise Exception(f"Expected type {self.__type}, found {type(item)}.")

        self.__size: int = kwargs.get("size") or len(items)
        if self.__size > len(items):
            # Pad array with `None`
            items = items + (None,) * (self.__size-len(items))
        elif self.__size < len(items):
            raise Exception(f"Array created with more items than specified")

        self.__arr = list(items)

    def __getitem__(self, idx):
        return self.__arr[idx]

    def __setitem__(self, idx, item):
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


if __name__ == "__main__":
    arr = Array(1, 2, 3, type=int, size=4)

    print(arr)
    print(len(arr))

    for item in arr:
        print(item)

    arr[3] = 10

    for item in arr:
        print(item)


