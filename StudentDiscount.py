from DiscountStrategy import DiscountStrategy
class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return max(0, total - 5)