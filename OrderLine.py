from Product import Product
class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.price() * self.__quantity