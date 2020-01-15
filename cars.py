# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom = {'Jeep Renegade', 'Kia Soul', 'Ford Thunderbird', 'Toyota Prius'}

# Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add('Ford Thunderbird')

# Print your showroom. Notice how there's still only one instance of that model in there.
# print(showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update(['Tesla Truck', 'Honda CRV'])
# print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard('Tesla Truck')
print(showroom)




#Acquiring more cars

#Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {'Jeep Renegade', 'Kia Soul', 'Ford Thunderbird', 'Toyota Corolla', 'Hyundai Sonata'}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
intersect_table = list(showroom & junkyard)

print("intersect_table:", intersect_table)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
union_set = showroom.union(junkyard)
# print("union:", union_set)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
union_set.discard('Toyota Corolla')
print("union:", union_set)