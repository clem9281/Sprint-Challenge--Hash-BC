#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    i = 0
    # get the first node in the hash table
    current_node = hash_table_retrieve(hashtable, "NONE")
    while i < length:
        route[i] = current_node
        current_node = hash_table_retrieve(hashtable, current_node)
        i += 1
    return route
