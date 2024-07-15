immutable_var = (2,4, True, "Hello")
print(immutable_var)
immutable_var = (2,4, True,"Hello")
print(immutable_var)
immutable_var = tuple([2,4,True,"Hello"])
print(immutable_var)

print(immutable_var[0])
#immutable_var [0] = 10
#print(immutable_var[10])  # в кортеже нет такого элемента

mutable_list = [3,5,False,"Goodbye"]
print (mutable_list)
print(mutable_list[-1])
mutable_list[-1] = "Hello"
print(mutable_list)