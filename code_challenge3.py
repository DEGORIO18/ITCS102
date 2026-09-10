# Global Freight Calculator

sender_name = input("Sender name:")
item_type = input("Type of Item:")
isFragile = input("True or False?")
weight = float(input("Weight: "))
distance = float(input("Distance: "))

is_express = bool(input("is it express shipping:"))
is_international = bool(input("is it international shipping:"))


base_cost = (weight * 2.50) + (distance * 0.25)
if weight <= 2.0 and distance <= 100:
     print("Total")

