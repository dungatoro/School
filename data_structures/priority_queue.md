# Priority Queue

In a priority queue, items can have different priority; higher priority items go 
before lower priority items.

One implementation of this is using multiple [[circular_queue]]s. This uses much 
more memory than a single queue, as it requires a different queue for each level 
of priority.
