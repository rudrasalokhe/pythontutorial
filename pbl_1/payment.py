class Payment:
    @staticmethod
    def process_payment(cart, payment_method):
        if cart.total > 0:
            print(f"Payment of ${cart.total} made using {payment_method}")
            return True
        print("Cart is empty. Cannot process payment.")
        return False
