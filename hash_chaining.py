class HashTable:

	def __init__(self, size = 101):
		self.data = [0 for _ in range(size)]
		self.size = size

	# returns the hashed value of the item
	# i.e. the index the item will be stored at
	def hash_val(self, item):
		return hash(item) % self.size

	# insert item into hash table
	def insert(self, item):
		hash_val = self.hash_val(item)
		self.data[hash_val] = item

	# returns true if item is in hash table
	def search(self, item):
		hash_val = self.hash_val(item)
		return self.data[hash_val] == item

hashTable = HashTable()
hashTable.insert('1000')
print(hashTable.search('100'))