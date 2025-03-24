class Discounts:
    COUPONS = {
        "SAVE10": 0.10,
        "SAVE20": 0.20,
    }
    
    @staticmethod
    def apply_discount(cart, coupon_code):
        if coupon_code in Discounts.COUPONS:
            discount = cart.total * Discounts.COUPONS[coupon_code]
            cart.total -= discount
            print(f"Discount Applied: ${discount}")
        else:
            print("Invalid Coupon Code")


# payment.py
class Payment:
    @staticmethod
    def process_payment(cart, payment_method):
        if cart.total > 0:
            print(f"Payment of ${cart.total} made using {payment_method}")
            return True
        print("Cart is empty. Cannot process payment.")
        return False