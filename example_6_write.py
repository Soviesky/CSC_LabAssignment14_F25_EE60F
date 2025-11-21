file_obj = open("data2.txt", "r")
file_obj.write("Hello, World!")
file_obj.close()
#you would see an error because we used the wrong open mode "r"
# in order to write a file, "w" or "a" should be used 