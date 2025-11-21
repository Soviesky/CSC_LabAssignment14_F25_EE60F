# create a file object of file "data1.txt" , with mode "r" which is "read"
file = open("data1.txt", "r")
file_object = open("data1.txt", "r")
print(file_object)

#you will see an error "FileNotFoundError" since file "data101.txt" does not exist
file_object_error = open("data101.txt", "r")
print(file_object_error)