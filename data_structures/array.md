# Array
An array is a fixed length data structure that stores values of the same type.

Arrays can be used to implement other data structures such as a [[stack]].

## Why the same type?

Values of the same type take up the same space in memory. This means that an item
at a given index can be calculated using the number of bytes needed to store that 
type * the index + the starting location of the array in memory.

