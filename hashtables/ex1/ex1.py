#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # must be a list of at least 2 weights
    if len(weights) < 2:
        print("ERROR: Must have at least 2 weights")
        return None
    # if there are only 2 they should equal limit
    elif len(weights) == 2:
        if weights[0] + weights[1] == limit:
            return [1, 0]
    # all other scenarios
    # insert the weights into the HT
    # def hash_table_insert(hash_table, key, value):
    else:
        for x in range(len(weights)):
            if ht is not None:
                hash_table_insert(ht, weights[x], x)

        # high = limit - weight
        #low = weight

        for weight in range(1, limit + 1):
            high = limit - weight
            low = weight
            # check if low value exists
            lowVal = hash_table_retrieve(ht, low)

            if lowVal is not None:
                highVal = hash_table_retrieve(ht, high)
                #check if high value exists
                if highVal is not None:
                    return [highVal, lowVal]





    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
