"""

Data Structure
- insert -> O(n)
- read -> O(1)
- delete -> O(n)

Hash table
- Dict
- Object (javascript)
- Map
- Hash maps

Hash table run times
- insert -> O(1) {{ sometimes worst case O(n) }}
- read -> O(1)
- delete -> O(1)

Hash Function!
- must take string -> number
- must always return same output for same input

"""

# d = {
#     'banana': 'is a fruit',
#     'apple': 'is also a fruit',
#     'pickle': 'vegetable'
# }

# storage = [None] * 8

# def hash_func(string, capacity):
#     bytes_str = string.encode()
#     num = 0
#     for byte in bytes_str:
#         # print(byte)
#         num += byte
#     return num % capacity

# index = hash_func('apple', 8)
# print(f"Apple hashed to {index}, store it there in stronger")
# print(hash_func('apple', 8))
# print(hash_func('banana', 8))

class Dict:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity

    def hash_func(self, key):
        bytes_str = key.encode()
        num = 0
        for byte in bytes_str:
            # print(byte)
            num += byte
        return num % self.capacity

    # O(1)
    def insert(self, key, value):
        # hash the key
        index = self.hash_func(key)
        self.storage[index] = (key, value)

    def get(self, key):
        # has the key to get the index
        index = self.hash_func(key)
        return self.storage[index][1] # 0(1)

    def delete(self, key):
        # has the key to get the index
        index = self.hash_func(key)
        self.storage[index] = None

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)

d = Dict(8)
# print(d.storage)

# d.insert("apple", "is a fruit")
d["apple"] = "is a fruit"
d["banana"] = "is also a fruit"
d["cucumber"] = "is a vegetable"
d["peach"] = "This is definitely not a banana"


print(d.storage)
print(d["apple"])
print(d["banana"])
