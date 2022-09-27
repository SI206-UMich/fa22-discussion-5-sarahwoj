import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a' or i == 'A':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		stock_max = 0
		max_stock_item = []
		for item in self.items:
			if item.self.stock > stock_max:
				stock_max = item.self.stock
				max_stock_item.append(item)
			else:
				pass

	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		price_max = 0
		max_price_item = []
		for item in self.items:
			if item.self.price > price_max:
				price_max = item.self.price
				max_price_item.append(item)
			else:
				pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("Burger"),0, "count_a('Burger') should return 0")
		self.assertEqual(count_a("Water"),1, "count_a('Water') should return 1")
		self.assertEqual(count_a("Fanta"),2, "count_a('Fanta') should return 2")
		self.assertEqual(count_a("Apple"),1, "count_a('Apple') should return 1")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.assertIn(self.item1.name, Warehouse().items, "Test of add_items")
		self.assertIn(self.item2.name, Warehouse().items, "Test of add_items")
		self.assertIn(self.item5.name, Warehouse().items, "Test of add_items")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.assertEqual([self.item1, self.item2, self.item3], 100,  "should return 100")
		self.assertEqual([self.item3, self.item4, self.item5], 100,  "should return 100")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual([self.item1, self.item2, self.item3], 6,  "should return 6")
		self.assertEqual([self.item3, self.item4, self.item5], 3,  "should return 3")
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()