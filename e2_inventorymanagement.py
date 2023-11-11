# -*- coding: utf-8 -*-
"""e2-InventoryManagement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/181xu-lDd07ddhb3j45HViUSjHwcSXZ_A

**Inventory Management**
"""

class InventoryManagement:
    def __init__(self, limit=50000):
        self.inventory = {}
        self.total_quantity = 0
        self.limit = limit

    def add_item(self, item, quantity, weight, height):
        if weight > 5:
            print("Weight limit exceeded. Maximum allowed weight is 5kg per item.")
            return
        if height > 25:
            print("Height limit exceeded. Maximum allowed height is 25 inches per item.")
            return
        if self.total_quantity + quantity > self.limit:
            print(f"Couldn't add item. Inventory limit: {self.limit}, current: {self.total_quantity}, tried to add: {quantity}")
            return

        if item in self.inventory:
            self.inventory[item]['quantity'] += quantity
        else:
            self.inventory[item] = {'quantity': quantity, 'weight': weight, 'height': height}

        self.total_quantity += quantity
        print(f"Added {quantity} {item}(s) to inventory.")

    def remove_item(self, item, quantity):
        if item in self.inventory and self.inventory[item]['quantity'] >= quantity:
            self.inventory[item]['quantity'] -= quantity
            self.total_quantity -= quantity
            print(f"Removed {quantity} {item}(s) from inventory.")
        else:
            print(f"Unable to remove {quantity} {item}(s) from inventory.")

    def check_inventory(self):
        print("Inventory Status:")
        for item, data in self.inventory.items():
            print(f"{item}: {data['quantity']}, weight: {data['weight']}, height: {data['height']}")

    def get_total_count(self):
        print(f"Total items in inventory: {self.total_quantity}")

    def is_inventory_full(self):
        return self.total_quantity >= self.limit

def main():
    inventory_system = InventoryManagement()

    while True:
        print("\n1. Check Inventory")
        print("2. Get Total Count")
        print("3. Remove Item")
        if not inventory_system.is_inventory_full():
            print("4. Add Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            inventory_system.check_inventory()

        elif choice == '2':
            inventory_system.get_total_count()

        elif choice == '3':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            inventory_system.remove_item(item, quantity)

        elif choice == '4' and not inventory_system.is_inventory_full():
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            weight = float(input("Enter the weight of the item (up to 5 kg): "))
            height = float(input("Enter the height of the item (up to 25 inches): "))
            inventory_system.add_item(item, quantity, weight, height)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

"""**Delivery Creation**"""

class InventoryManagement:
    # ...Existing code...
    def get_item_details(self, item):
        return self.inventory.get(item, None)

# ...Existing code...
class DeliveryManagement:
    def __init__(self, inventory_system):
        self.delivery_data = {}
        self.inventory_system = inventory_system

    def create_delivery(self):
        # ...Existing code...

        item = input("Enter item name for delivery from inventory: ")

        item_details = self.inventory_system.get_item_details(item)
        if item_details is not None:
            self.delivery_data[delivery_number]['item_details'] = item_details
        else:
            print(f"Item {item} does not exist in the inventory.")

        print("\nDelivery created successfully!")

    def get_delivery(self, delivery_number):
        if delivery_number in self.delivery_data:
            print(f"\nDelivery Details for {delivery_number}: ")
            for k, v in self.delivery_data[delivery_number].items():
                if k == 'item_details':
                    print(f"{k}: ")
                    for k1, v1 in v.items():
                        print(f"    {k1}: {v1}")
                else:
                    print(f"{k}: {v}")
        else:
            print("No such delivery number exists!")

def main():
    inventory_system = InventoryManagement()
    delivery_system = DeliveryManagement(inventory_system)

    # ...Existing code...

if __name__ == "__main__":
    main()