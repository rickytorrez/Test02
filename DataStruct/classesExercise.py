class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {
            'name':name,
            'price': price
        }
        self.items.append(item)

    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total
        return sum([item['price'] for item in self.items])
        