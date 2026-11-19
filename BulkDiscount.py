from DiscountStrategy import DiscountStrategy
class BulkDiscount(DiscountStrategy):

    def __init__(self, threshold, amount):
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.amount
        return total