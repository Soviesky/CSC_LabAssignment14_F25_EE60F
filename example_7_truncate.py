# please open "data2.txt" to see the file content because it will be overwritten
file_obj = open("data2.txt", "w")

#method write() would overwrite the existing content of the file
file_obj.write("hello world")
file_obj.write("!")

#there is no blank space between the written contents in above two lines

file_obj.close()
#please open "datat2.txt" again to see the file content