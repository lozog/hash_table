# a hash table implementation with linear probing

class HashTable:

	def __init__(self, size = 101):
		self.data = [None for _ in range(size)]
		self.size = size

	# returns the hashed value of the item
	def __hash_val(self, item):
		return hash(item) % self.size

	# insert item into hash table
	def insert(self, item):
		hash_val = self.__hash_val(item)

		for i in range(self.size):
			if self.data[hash_val] is None:
				self.data[hash_val] = item
				return
			else:
				hash_val = (hash_val + 1) % self.size

		raise RuntimeError("Hash table is full - could not insert")

	# returns true if item is in hash table
	def search(self, item):
		hash_val = self.__hash_val(item)
		return item in self.data[hash_val]