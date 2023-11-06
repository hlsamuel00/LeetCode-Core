from random import choice
from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        # Initialize collection to a dictionary with list values
        self.collection = defaultdict(list)

        # Initialize the random list to an empty list
        self.rand_list = []

    def insert(self, val: int) -> bool:
        # Collect the index the value will have in the rand_list
        rand_idx = len(self.rand_list)

        # Collect the index the value will have in its internal list
        coll_idx = len(self.collection[val])

        # Append the random list index to the collection list
        self.collection[val].append(rand_idx)

        # Append a tuple of the value and the index it has on the collection list to the random list.
        self.rand_list.append((val, coll_idx))

        # Return a boolean value of whether the collection list only contains one item (if so, the value was not already in the dictionary)
        return len(self.collection[val]) == 1

    def remove(self, val: int) -> bool:

        # If val is not in the dictionary, return False
        if val not in self.collection:
            return False

        # Collect the index that val has in rand_list
        val_idx = self.collection[val][-1]

        # Collect the last element and the index the item has in its collection list
        last_element, coll_idx = self.rand_list[-1]

        # Update the index in the collection list to the new index
        self.collection[last_element][coll_idx] = val_idx
       
        # Update the rand_list at the value index to the last element in rand_list
        self.rand_list[val_idx] = self.rand_list[-1]

        # Pop off the last item in rand_list
        self.rand_list.pop()
       
        # Pop off the last item in the collection list
        self.collection[val].pop()
       
        # If the collection list is empty, delete the value from the dictionary
        if not self.collection[val]:
            del self.collection[val]

        # Return True because the value was in the dictionary
        return True

    def getRandom(self) -> int:
        # Return the first value in the random tuple chosen from rand_list
        return choice(self.rand_list)[0]