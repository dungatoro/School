# Linear Queue

A linear queue solves the memory problem of the naive queue by shifting items 
down after each dequeue. This is a solution but not a very good one, shifting 
requires lots of shuffling of data each dequeue.

A [[circular_queue]] is the best implementation of a queue, it fixes both 
problems but is more complex to implement.
