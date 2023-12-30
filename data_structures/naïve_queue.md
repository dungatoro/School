# Naïve Queue

The naïve implementation has two pointers at the head and tail. When dequeuing, 
the head pointer is incremented and when endqueuing the tail pointer is 
incrememented; this results in the capacity of the queue decreasing each time an 
item is dequeued.

A [[linear_queue]] aims to solve this problem.


