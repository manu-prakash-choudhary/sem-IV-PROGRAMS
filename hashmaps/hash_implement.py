class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        if type(key) == str and key.isalpha():
            return sum([ord(c) for c in key]) % self.size
        elif type(key) == int:
            return key % self.size
        else:
            raise ValueError("Key should be a string or integer")

    def add(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError("Key not found")

    def __repr__(self):
        return repr(self.table)
    
    


# Example usage
hash_table = HashTable(10)
hash_table.add('apple', 5)
hash_table.add('banana', 7)
hash_table.add('orange', 3)

print(hash_table)  # Output the hash table

print(hash_table.get('apple'))  # Output: 5
print(hash_table.get('banana'))  # Output: 7
print(hash_table.get('orange'))  # Output: 3
