from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
class ProductFactory: 
    @staticmethod 
    def create(product_id: str, name: str, price: float, stock: int, weight: float, type: int, supplier: Supplier) -> Product: 
        if type == 1: 
            return PhysicalProduct(product_id, name, price, stock, weight, type, supplier) 
        elif type == 2: 
            return DigitalProduct(product_id, name, price, stock, weight, type, supplier) 
        else: 
            raise ValueError(f"Unknown product type: {type}")