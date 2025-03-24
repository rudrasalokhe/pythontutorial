from collections import defaultdict
from product import Product

class Cart:
    def __init__(self):
        self.items = defaultdict(int)
        self.total = 0.0
    
    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.items[product] += quantity
            self.total += product.price * quantity
        else:
            print(f"Not enough stock for {product.name}")
    
    def remove_product(self, product, quantity):
        if self.items[product] >= quantity:
            self.items[product] -= quantity
            product.stock += quantity
            self.total -= product.price * quantity
        else:
            print(f"Cannot remove {quantity} of {product.name}")
            
    def view_cart(self):
        for product, quantity in self.items.items():
            print(f"{product.name} x {quantity} = ${product.price * quantity}")
        print(f"Total: ${self.total}")
