# List iniciallization

list_1 = []			# empty list
list_2 = list()		# empty list

###############################
	# Data Binding
###############################

even1  = [2, 4, 6, 8]
even2 = even1		# >>> even2 is even1		>>> True

print(even2 is even1)
even2.sort(reverse=True)
print(even)
# Changes done in even2 will change even1 vic versa, this is called Data Binding




x1= [1,2,3,4,5,6,90,1,54,78,6,34]
print(x1)
x1.sort() # .sort doestnot create a new list (obj) but change the existing list
print(x1)

