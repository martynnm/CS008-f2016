/**
 * Created by martyn on 9/30/2016.
 */
I began my thought process for this program by finding a way to determine whether the user wanted to use the USC or
Metric system. I wanted to limit the amount of possible responses the user could give to avoid any error so I asked
if they would like to use USC over Metric in a simple yes or no prompt, if they said yes I would use USC if not I would
automatically put them into the Metric path of my program. I placed this under an if statement of if statement==y then
the user would be taken down the USC pathway followed later on by an elif statement if statement==n.I also wanted to
limit the number of responses the user had to give to once again  avoid error. So I asked them for the only two things
I needed: the distance they travelled and the amount of gas they used. Based on what system they used I converted the
given numbers to the opposite system ( if they said to use USC I converted to Metric and vice-versa). Once I converted
both the distance and the gas used I calculated the mpg and km/100liters. Of course I did this all with placing these
stats to variables in my code so I could later use them to output the info to the user. Once I had all of the gathered
information I presented the table that was required. Since all of the values all required no thousand separators, and
three decimal places I grouped each line needed into one string and formatted all of the numbers in that line with one
    command to lessen the amount of code needed using print (x/ty/tz.format).Using \t and formatting the entire line
allowed me to not have to write as much code as I may have if I used spaces and formatted every individual value
separately. After this I used if and elif statements to determine what fuel efficiency rating the user will receive
( i used elif since there were a number of possibilities and ranges that the consumption could fall under.)
After writing this path I then went back to the original indentation of my if statement and made an elif statement for
    if the user typed n and requested to use the Metric pathway. This pathway was exactly the same as my original USC
pathway except the first two units that I requested from the user were kilometers and liters and not miles and gallons.