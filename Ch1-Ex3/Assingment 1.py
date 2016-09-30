#First we must ask whether the user wants to use the USC or Metric system
system = input("If you would like to use USC over metric type y if not type n:")
#Now that we have what system to use we will find their distance and gas usage
if system == 'y':
    distance=((float(input("How many miles did you drive?"))))
    fuel=((float(input("How much gas in gallons did you use?"))))
#We will now calculate the mpg and the Metric conversion units
    mpg=distance/fuel
print(mpg)
