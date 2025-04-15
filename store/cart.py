# store/cart.py

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
        else:
            self.cart[product_id] = {
                "title": product.title,
                "price": str(product.price),
                "quantity": quantity,
            }
        self.save()

    def remove(self, product_or_key):
        product_id = str(product_or_key.id) if hasattr(product_or_key, 'id') else str(product_or_key)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

    def save(self):
        self.session.modified = True

    def items(self):
        return self.cart.items()

    def total(self):
        return sum(float(item["price"]) * item["quantity"] for item in self.cart.values())
