# set: collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife"}      # one set
dishes = {"bowl", "plate", "cup"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))


# for x in utensils:
#     print(x)