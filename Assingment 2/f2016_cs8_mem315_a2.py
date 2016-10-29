# This loop will accept the input given by the user as a file found on the computer
def processfile(file):
    # we must first set a list of begining variables (Each will start at the value of 0 so the data of the value of the file will be added onto this 0 state
    excel1 = []
    # This variable counts the lines of the files a
    linec = 0
    # This variable counts the value of the distance run
    distance_ran = 0
    # We set a command that sets the file found equal to a variable, the string of r is set so the file is set to read only
    f = open(file, 'r')
    for line in f:
        # Count below allows the program to add one to our counter everytime it reads a line
        linec += 1
        # Removes the trailing characters found in the line
        line = line.rstrip()
        # This allows us to split column 1 and 2 from one another as seperate entries on the same list
        line = line.split(',')
        # This allows us to add the value of the string (converting it to a float) found in column 2 of our files to the pre-established variable of distance_ran
        distance_ran += float(line[1])
        # We will now return the values found in the loop
    excel1.append(linec)
    excel1.append(distance_ran)
    # Closing the file
    f.close()
    # Returns the values found in the loop to the main function
    return excel1


# This allows the format of the information derived from the read files in regards to things such as spacing
def printKV(key, value, klen):
    key_key = len(key)
    # Here we are checking to see which is klen or the original length of the key and set
    if klen > key_key:
        key_key = klen
    # this final cluster is simply formatting the key such as file read to the amount of spaces we require to fit our formatting requirments
    key = format(key, str(key_key) + 's')
    if isinstance(value, str) == True:
        # the 30s allows us to take any value that we are printing to truncate whatever amount of spaces we require
        value = format(value, '.30s')
    elif isinstance(value, float) == True:
        value = format(value, '.3f')
        # Here we are moving the second column to the right and making it ten characters long while also truncating it to 3 decimal places
        value = format(str(value), '>10s')
    elif isinstance(value, int) == True:
        value = format(str(value), '>10s')
    print(key + ' : ' + value)


def main():
    # Begin loop
    file = True
    # Here we set the variable for the total lines and distance that will be displayed when the user quits the program
    total_lines = 0
    total_distance = 0
    # Here we are begining the loop that will process each inputed file until one of the specific preset commands are made
    while file:
        file = input('Please provide the file name : ')
        print(' ')
        if file == '' or file == 'quit' or file == 'q':
            printKV('Total # of lines', total_lines, 28)
            printKV('Total distance ran', total_distance, 28)
            break
        # This is the returned list from the function processfile that contains the line count and the distance ran for the corresponding file
        list1 = processfile(file)
        total_lines += list1[0]
        total_distance += list1[1]
        # Here we print the three things required for the user the th
        printKV('File read', file, 28)
        printKV('Partial Total # of lines', list1[0], 28)
        printKV('Partial distance run', list1[1], 28)
        print('')
        print('')


main()









