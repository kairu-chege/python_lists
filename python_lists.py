# initialize an empty list 
my_list = []
# appending the empty list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# inserting 15 at the second position in the list 
new_element = 15
my_list.insert(2, new_element)

print(my_list)

# extending my_list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)

print(my_list)

# removing the last element from my_list
my_list.pop()
print(my_list)

#sorting my_list in ascending order usig the sorted() function
sorted_list = sorted(my_list)
print(sorted_list)

#findinf and printing the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of the value 30 is: {index_of_30}")