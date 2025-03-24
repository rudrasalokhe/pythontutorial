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


