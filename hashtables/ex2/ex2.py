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
    #First ticket source is 'NONE'
    source = "NONE"
    #Last ticket destination is 'NONE'
    
    # put all tickets in a hashtable
    # source is key, dest is the value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    for x in range(length):
        orderedTickets = hash_table_retrieve(hashtable, source)
        # set the next key to the source of next ticket
        source = orderedTickets
        # add it to the route array in proper order
        route[x] = orderedTickets

            

    return route
