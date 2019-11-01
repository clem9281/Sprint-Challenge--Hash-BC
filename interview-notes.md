#### ARRAY

- Sequence of contiguous memory
- Access: O(1) due to indexing
- Add/remove from front: O(n) due to shifting
- Remove from end: O(1)
- Add to end: you have to go get an entirely new block of memory

#### HASH TABLE

- key value with access of O(1)
- under the hood we store it in an array of length capacity
- capacity is to help deal with memory load of array - shorter the array more collisions though
- each key value is stored at array[hash(element) % capacity]
- stored as a linked list to handle collisions
- when we hit capacity double capacity rehash

#### BLOCK CHAIN

- block contains relevant info, like transactions, timestamp, and most importantly the hash of the previous block
- this makes it hard to forge or alter transactions, but not impossible so we also have the concept of proof of work
- miners have to solve hash puzzles that add time to the verification process
