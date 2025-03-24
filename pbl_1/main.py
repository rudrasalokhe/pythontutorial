from product import Product
from cart import Cart
from discounts import Discounts
from payment import Payment

if __name__ == "__main__":
    p1 = Product("Laptop", 1000, 10)
    p2 = Product("Phone", 500, 5)
    
    cart = Cart()
    cart.add_product(p1, 2)
    cart.add_product(p2, 1)
    cart.view_cart()
    
    Discounts.apply_discount(cart, "SAVE10")
    cart.view_cart()
    
    Payment.process_payment(cart, "Credit Card")
