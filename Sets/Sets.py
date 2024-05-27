# set = collection which is unordered, unindexed and no duplicate values

utentsils = {"fork", "spoon", "knife"}
dishes = {"plate", "bowl", "mug", "spoon"}

#you can do this either way you want
#utentsils.update(dishes)

#like a standard list
#utentsils.add("hammer")
#utentsils.remove("fork")
#utentsils.clear()

#creating a new set
dinner_table = utentsils.union(dishes)

#for x in utentsils:
 #   print(x)
  
#for i in dinner_table:
 #   print(i)  

#compares the two sets and shows what utentsils has that dishes doesn't have
#print(utentsils.difference(dishes))

#Will show what the two sets have in common
print(dishes.intersection(utentsils))