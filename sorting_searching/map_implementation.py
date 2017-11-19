""" Map interface implementation using hash table"""


class HashTable(object):
    """
    Hash table class implementation
    """
    def __init__(self):
        # no of items in hash table
        self.size = 11
        # slots will hold key item
        self.slots = [None] * self.size
        # corresponding position in data will hold value
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            # If slot is empty, add key and value
            # to slots and data lists
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                # If key is already present, then update value
                self.data[hash_value] = data
            else:
                # Computer next slot's position
                next_slot = self.rehash(hash_value, self.size)

                # Iterate till next empty slot is found
                while (self.slots[next_slot] is not None and
                       self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, self.size)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        # Start at initial slot
        start_slot = self.hash_function(key, self.size)
        data, found, stop = None, False, False
        position = start_slot

        # Iterate in the hash table slots
        # Check all posible slots that could have been
        # populated using linear probing
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # If key not found, rehash to get next slot
                position = self.rehash(position, self.size)
                # If after rehashing no key found and 
                # we reach the start slot then item is not found.
                if position == start_slot:
                    stop = True
        
        return data

    def hash_function(self, key, size):
        """
        Implements modulo arithmetic/remainder method
        returns: remainder of dividing item with size of
        hash table
        """
        return key % size

    def rehash(self, old_hash, size):
        """
        Computer a new hash using standard linear probing with
        1
        """
        return (old_hash + 1) % size

    def __getitem__(self, key):
        """
        Support for map[key] notation
        """
        return self.get(key)

    def __setitem__(self, key, data):
        """
        Support for map[key] = value notation
        """
        return self.put(key, data)


if __name__ == '__main__':
    map_ = HashTable()
    map_.put(25, 'Hello')
    print(map_.get(25))
