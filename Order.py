from Product import Product
from OrderLine import OrderLine
from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount
        
    def calculate_total(self) -> float:
        total = 0.00
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        discounted_total = self.discount.apply(total)
        return round(discounted_total, 2) #return total to 2 decimal points

    def display_order(self) -> None:
        print("Order Id:", self.order_id)
        for order_line in self.order_lines:
            print("Subtotal: $", order_line.calculate_subtotal())
        print("Total: $", self.calculate_total())

    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self.order_lines):
            self.order_lines.pop(index)
        else:
            print("Invalid order line index")