# a hash table implementation with chaining

class HashTable:

	def __init__(self, size = 101):
		self.data = [[] for _ in range(size)]
		self.size = size

	# returns the hashed value of the item
	# i.e. the index the item will be stored at
	def __hash_val(self, item):
		return hash(item) % self.size

	# insert item into hash table
	def insert(self, item):
		hash_val = self.__hash_val(item)
		self.data[hash_val].append(item)

	# returns true if item is in hash table
	def search(self, item):
		hash_val = self.__hash_val(item)
		return item in self.data[hash_val]
