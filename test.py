import json
import os
import csv
from Product import Product
from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory
from Supplier import Supplier
from Order import Order
from CanBeShipped import CanBeShipped
from DiscountStrategy import DiscountStrategy
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
from StudentDiscount import StudentDiscount
from ProductFactory import ProductFactory

supplier1 = Supplier(101, "ABC Supplies", "abc@gmail.com")
supplier2 = Supplier(102, "DEF Supplies", "def@hotmail.com")
supplier3 = Supplier(103, "GHI Supplies", "ghi@gmail.com")
inventory_A = Inventory()
inventory_B = Inventory()
inventory_C = Inventory()
inventory = Inventory()
order1 = Order("0001")
order2 = Order("0002")
product1 = ProductFactory.create("P001", "Laptop", 1200.00, 15, 37.00, 1, supplier1)
product2 = ProductFactory.create("P002", "Mouse", 25.50, 40, 0.50, 2, supplier2)
print(product1)
print(product2)

def show_product_details(product: Product) -> None:
    product.display_information()
    product.get_fulfilment_info()
print("Start of Lab 8 Tests")
print("Association & Aggregation Test")
del supplier1
del supplier2
inventory_A.add_product(product1)
inventory_A.add_product(product2)
print("Inventory A")
inventory_A.display_all()
inventory_A.remove_product("P001")
print("P001 removed")
inventory_A.display_all()
print("P001 Info")
product1.display_information()
inventory_B.add_product(product1)
print("Inventory B")
inventory_B.display_all()
inventory_B.remove_product("P001")
print("P001 removed")
inventory_B.display_all()
print("P001 Info")
product1.display_information()
product2.display_information()
product1.get_fulfilment_info()
product2.get_fulfilment_info()
print("End Association & Aggregation Test\n")

if isinstance(product1, CanBeShipped):
    product1.calculate_shipping_cost()

print("\nComposition Test")
order1.add_order_line(product1, 2)
order1.add_order_line(product2, 3)
print("Order 1")
order1.display_order()
order2.add_order_line(product1, 2)
print("Order 2")
order2.display_order()
order1.remove_order_line(0)
print("Order 1")
order1.display_order()
print("End Composition Test\n")

#Lab 8 Part 6.2
print("Part 6.2 Test substitutability")
show_product_details(product1)
show_product_details(product2)
print("End Test substitutability\n")

#Lab 8 part 7.2
inventory_C.add_product(product1)
inventory_C.add_product(product2)
inventory_C.display_all()
print("End of Lab 8 Tests")

#Lab 9 part 2.3
print("\nStart of Lab 9 Tests")
print("Lab 9 part 2.3 Test")
order3 = Order("0003", BulkDiscount(200, 20))
order3.add_order_line(product1, 3)
order3.add_order_line(product2, 2)
print("Bulk discount (200,20)")
order3.display_order()
order3.set_discount(PercentageDiscount(10))
print("Percentage discount 10%")
order3.display_order()
print("End Lab 9 part 2.3 test")

print("\nLab 9 part 2.4 Student Discount Test")
order3.set_discount(StudentDiscount())
print("Student Discount ($5 off)")
order3.display_order()
order4 = Order("0004")
order4.add_order_line(product1, 3)
order4.add_order_line(product2, 2)
discount = PercentageDiscount(10)
order3.set_discount(discount)
order4.set_discount(discount)
order3.display_order()
order4.display_order()
print("End Lab 9 part 2.4 test")

print("\nLab 9 part 5.2 test")
def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                try:
                    product_id = row[0]
                    name = row[1]
                    price = float(row[2])
                    stock = int(row[3])
                    value = float(row[4])
                    product_type = int(row[5])
                    product = ProductFactory.create(product_id, name, price, stock, value, product_type, supplier)
                    inventory.add_product(product)   # Add product to Inventory
                    loaded += 1
                except ValueError as e:
                    print(f"Invalid product row {row}: {e}")
                    continue
                except (IndexError, TypeError) as e:
                    print(f"Invalid product row {row}: {e}")
                    continue
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")

load_products("products.csv", inventory, supplier3)
load_products("products_renamed.csv", inventory, supplier3)
print("End of Lab 9 part 5.2 test")
print("End of Lab 9 Tests")