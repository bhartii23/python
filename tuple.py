# Tuple declearation
t=()

# check type
print(type(t))


# put data in Tuple
t1=(1,2,"hello",True,5+6j)


# print tuple
print(t1)


# Tuple and list first difference bracket type
# list = [] and Tuple = ()
# accessing element in tuple using indexing operation
# always use [] for index operation
print(t1[2])


# Tuple and list second difference is mutability
# i.e. we cannot change data 
# tuples are used when data has not to change , it should be permanent and unchangeble .

# converting tuple into string
t1_t = list(t1)
print(list(t1_t))
print(t1_t.append(12)) 
print(t1_t)
# converting list into tuples
# print(tuple(list_name))
# tuples have only two functions 
# 1)count , 2)index
print(t1.count("hello"))
print(t1.index("hello"))
# min() , max() also used .
# len() also used