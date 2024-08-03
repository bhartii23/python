l=[12,34,"Good Morning",True,4+9j]

# printing list
print(l)


# extracting element by mentioning index number
print(l[3])


# printing elements from nth to mth 
# nth<=list_elements<mth
print(l[1:3])


# reversing list 
# temperory reversing
print(l[::-1])


# replacing element by another element / new element
# in string we cannot perform this operation to change letter
l[3]="python"
print(l)


# changing elements between (n-1)th to mth
l[2:4]="good","best"
print(l)


# printing one list 'n' times
print(l*3)


# joining 'n' number of lists 
# list + list = valid
# list + datatypes = invalid
l1=[12,34,56]
l2=["nice",9+12,3j]
l3=l+l1+l2
print(l3)


# printing length of list
# Function = len()
print(len(l))


# searching element in list
# Function = element in list_name
print(12 in l1)


# finding maximum in list 
# Function = max(l1)
print(max(l1))


# finding minimum in list 
# Function = min(l1)
print(min(l1))


# you can't use max() , min() , sort() function in mixed datatype element's list


# sorting list
# sorting in ascending order 
# Function = list_name sort()
# print(l1.sort())


# sorting in descending order 
# Function = list_name sort(reverse=True)
# print(l1.sort(reverse=True))



# Adding element as last element
# Function = list_name append(adding_element)
print(l1.append("This is added element"))
print(l1)



# inserting element at nth position
# Function = List_name insert(nth,adding_element)
print(l1.insert(2,34.67))
print(l1)


# permanent reversing
# Function = .reverse()
# print(l2.reverse())


# deleting last element
print(l2.pop())
print(l2)


# deleting nth element
print(l2.pop(1))
print(l2)


# accessing element which in list which is added in another list
# print(l3[1][2]