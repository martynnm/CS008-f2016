/**
 * Created by martyn on 11/27/2016.
 */
Martyn Megaloudis
CS008
I began this process by writing a function that would be able to read the two columns provided by every file that was provided for this project.
    I first set two base values of linec and distance_ran of both zero so that I can add values that are read from the files to these variables.
    After reading the amount of lines in the file I used line=line.split (‘,’) to split the two columns of the excel document in half since the format of the excel document was actually (Name, Distance ran).
We then used +=float(line[1]) to add the value and converting it into a float and adding it to the base value of the distance_ran.
    So far we have written a function which splits the two data points in the files given to us reading the number of lines the file contains along with the addition of the value  found in column 2 (the distance ran) to our base variable of distance_ran.
    There is no need to retype this block of code for our second assignment since we know now we can just loop the function until the user enters a specific input to our program.
    Now I needed to write about a function that could be called when the user wanted to quit so that I could display the total lines and total distance of all the files that the user has inserted.
    Using if-elif statements I could cut out any extra spaces that were not needed. Using value=format(str(value), ‘>10s’) I could make the printed right column of the final count to ten characters long while also rounds it to three decimal points.
    Using isinstance, value= format(str(value,) and key=format we were able to define printKVS using the key and values presented in whatever file the user asks us to read and place it in the two column format that the assignment asks for.
After I defined the two functions to both retrieve the information from the files and print them in the correct format I could now begin to define the main function of the program.
    For the final count I decided to get another set of base values for total_lines and total_distance (so that like the previous base values I could simply add the information learned from the finals read can be added to the base values of zero).
I ask the user for the file and if they print any of the specified end results I can call the printKV function and add up and display all of the information that had so far been entered into the program.
    If they do not ask to quit the file and simply enter the file name that wants to be read I can return the functions to read and split the file and return the function that prints the partial information of that file.
    I looped the main function so the function continually loops until the user enters the specified end input.
