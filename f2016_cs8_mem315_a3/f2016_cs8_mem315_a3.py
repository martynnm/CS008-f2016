#Here we take the file name from the master file list. We also set initial values for each file to refer to the dictionary/count lines
def processFile(file):
    dict1 = {}
    appearances_dict = {}
    lines_read = 0
    max1 = ['Name', 0]
    min1 = ['Name', 1000000000]
    #Here we open 1/3 of the example files and set it to be read
    f = open(file, 'r')
    for line in f:
        lines_read += 1
        #Here we split each line at the comma and delete the white space
        line = line.rstrip()
        line = line.split(',')
        #Here we use this clause to remove counting the "Name" box to avoid any processing errors.
        if line[0] != 'name':
            name = str(line[0]).rstrip()
        #Here we take the second entry in the list which is the distance run and convert it into a float
            distance_run = float(line[1])
            if distance_run > max1[1]:
                max1[0] = name
                max1[1] = distance_run
        #Here, using the next two if functions we find the minimum and maximum distance run of the file we are reading
            if distance_run < min1[1]:
                min1[0] = name
                min1[1] = distance_run
            if name in dict1:
                dict1[name] += distance_run
                appearances_dict[name] += 1
        #This else clause allows us to find duplicates within the file and stop our dictionary from overwriting duplicate data entries
            else:
                dict1[name] = distance_run
                appearances_dict[name] = 1
    f.close()
    return [dict1, lines_read, max1, min1, appearances_dict]
#Here we return the values of the dictionary of the data of the file we just read. These are the persons name,how much they ran,number of lines read, 
#and the minimum and maximum of the file we just read
def printKV(key, value, klen):
    key_length = len(key)
    if klen > key_length:
        key_length = klen
    key = format(key, str(key_length)+'s')
    if isinstance(value, str) == True:
        value = format(value, '.30s')
    elif isinstance(value, float) == True:
        value = format(value, '.5f')
        value = format(str(value), '.30s')
    else:
        value = format(str(value), '.30s')
    print(key+' : '+value)

def main():
    #Here we are setting up the initial values for the dictionary
    main_dict = {}
    main_appearances_dict = {}
    total_files = 0
    total_lines = 0
    total_distance = 0
    main_max = ['Name', 0]
    main_min = ['Name', 1000000000]
    #Here we open and set up to read the master input list
    f = open('f2016_cs8_a3.data.txt', 'r')
    for line in f:
        total_files += 1
        file = line.rstrip()
        file = str(file)
        #here we call a function to retrieve the information required from the final 
        info = processFile(file)
        #Here we set up a new dictionary dict1 from our read file to the main function
        dict1 = info[0]
        appearances_dict = info[4]
        total_lines += info[1]
        #Here we are checking if a name from one file correlates to another file
        keys_list = list(dict1.keys())
        #Here we are figuring out if a key for one file is already in another file, if not we initilize it if so we are adding this key to the previous value
        for i in range(len(keys_list)):
            if keys_list[i] in main_dict:
                main_dict['{}'.format(keys_list[i])] += dict1['{}'.format(keys_list[i])]
                main_appearances_dict['{}'.format(keys_list[i])] += appearances_dict['{}'.format(keys_list[i])]
            else:
                main_dict['{}'.format(keys_list[i])] = dict1['{}'.format(keys_list[i])]
                main_appearances_dict['{}'.format(keys_list[i])] = appearances_dict['{}'.format(keys_list[i])]
        #We're checking the minimum and maximum values from our process function to see if they exceed/or are less than our pre-established global main and min
        if info[2][1] > main_max[1]:
            main_max[0] = info[2][0]
            main_max[1] = info[2][1]
        if info[3][1] < main_min[1]:
            main_min[0] = info[3][0]
            main_min[1] = info[3][1]   
    main_keys_list = list(main_dict.keys())
    #Here we are going send over the value from each key from our previous dictionary to our total distance
    for i in range(len(main_keys_list)):
        total_distance += main_dict[main_keys_list[i]]
        #Here we se the clause that if a key is one we delete that entry because we are only intrested in repeeat names
        if main_appearances_dict[main_keys_list[i]] == 1:
            del main_appearances_dict[main_keys_list[i]]
    f.close()
    #Printing the data read from our dictionary and main_keys_list
    printKV('Number of Input files read', total_files, 28)
    printKV('Total number of lines read', total_lines, 28)
    print('')
    printKV('total distance run', total_distance, 28)
    print('')
    printKV('max distance run', main_max[1], 28)
    printKV(' by particpant', main_max[0], 28)
    print('')
    printKV('min distance run', main_min[1], 28)
    printKV(' by participant', main_min[0], 28)
    print('')
    printKV('Total number of participants', len(main_dict), 28)
    print('Number of participants')
    printKV('with multiple records', len(main_appearances_dict), 28)
    #Here we are writing a new file,looping over all the keys in our dictionary and writing the data needed into this new file
    f = open('f2016_cs8_mem315_a3.data.output.csv', 'w')
    for i in range(len(main_keys_list)):
        #Here we are checking to see how many appearances a person has by looking in our apperances dictionary and if they are not we set our appearances to 1
        if main_keys_list[i] in main_appearances_dict:
            f.write('{},{},{:.2f}'.format(main_keys_list[i], main_appearances_dict[main_keys_list[i]], float(main_dict[main_keys_list[i]])) + '\n')
        else:
            f.write('{},{},{:.2f}'.format(main_keys_list[i], 1, float(main_dict[main_keys_list[i]])) + '\n')       
    f.close()
    
main()
    
