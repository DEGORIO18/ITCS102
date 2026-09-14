# Global Freight Calculator

sender_name = input("Sender name: ")
item_type = input("Type of Item: ")

is_fragile = input("Is it Fragile? True or False: ").upper() == "TRUE"

weight = float(input("Weight: "))
distance = float(input("Distance: "))

is_express = input("Is it Express shipping? True or False: ").upper() == "TRUE"

is_international = input("Is it International shipping? True or False: ").upper() == "TRUE"


base_cost = (weight * 2.50) + (distance * 0.25)


print("\n--- SHIPPING DETAILS ---")
print("Sender:", sender_name)
print("Item:", item_type)
print("Is it Fragile:", is_fragile)
print("Weight:", weight)
print("Distance:", distance)


if weight <= 2 and distance <= 100 and not is_express and not is_international:
    print("Shipping rate: Free shipping")
    print("Total cost: $0.00")

elif is_express and is_international:
    print("Shipping rate: International Express")
    print("Total cost:", (base_cost * 1.40) + 50)

elif is_express or (is_international and weight > 20):
    print("Shipping rate: Express or Heavy International")
    print("Total cost:", (base_cost * 1.20) + 25)

elif weight > 30 or distance > 1000:
    print("Shipping rate: Oversized")
    print("Total cost:", base_cost + 30)

else:
    print("Shipping rate: Standard")
    print("Total cost:", base_cost)