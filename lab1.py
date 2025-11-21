"""
Please open file "lab1_file.txt" to see the file structure.
The first line of the file indicates how many data lines in the file, say n.
The following n lines are the data lines, each line has a number.

The program reads the file "lab1_file.txt", and calculate average number of all those data line.
"""


def computer_average(filename):
    file_obj = open(filename, "r")
    # TODO: create a file object called "file_obj"
    # TODO: the file object opens the file passed by the argument "filename"
    # TODO: use open mode "r"

    # read file line, which is number of lines
    first_line = file_obj.readline()
    nums_line = int(first_line)
    # TODO: convert the variable `first_line` into an integer called `nums_line`

    # create a list to wrap all following numbers
    numbers = []

    for i in range(nums_line):
        line = file_obj.readline()

        # TODO: read one line in each iteration, read as a float number
        # TODO: append the float number into the list `numbers`


    # TODO: close the file object

    file_obj.close()
    
    # TODO: calculate the average of all numbers in the list, save the result to variable `avg`
    
    return avg


if __name__ == "__main__":
    average = computer_average("lab1_file.txt")
    print(average)
