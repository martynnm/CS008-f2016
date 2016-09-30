#First we must ask whether the user wants to use the USC or Metric system
system = input("If you would like to use USC over metric type y if not type n:")
#Now that we have what system to use we will find their distance and gas usage
if system == 'y':
    distance=((float(input("How many miles did you drive?"))))
    fuel=((float(input("How much gas in gallons did you use?"))))
#We will now calculate the mpg and the Metric conversion units
    mpg=distance/fuel
    mdistance=distance*1.60934
    mfuel=fuel*3.78541
#We will now calculate Metric Consumption
    mcm=mfuel/mdistance*100
#We will now present the user with their statistics in both USC and Metric
    print('                     \tUSC         \tMetric')
    print('Distance___________: \t{:.3f} miles\t{:.3f} Km'.format(distance, mdistance))
    print('Gas________________: \t{:.3f} gallons\t{:.3f} Liters'.format(fuel, mfuel))
    print("Consumption________: \t{:.3f} mpg\t    {:.3f} 1/100Km".format(mpg, mcm))
#Now using the guidlines provided we can give the user a gas consumption rating
    if mcm >20: print('Gas Consumption Rating:Extremely poor')
    elif 15< mcm <=20: print('Gas Consumption Rating:Poor')
    elif 10< mcm <=15: print('Gas Consumption Rating:Average')
    elif 8< mcm <=10: print('Gas Consumption Rating:Good')
    elif mcm <=8: print('Gas Consumption Rating:Excellent')
elif system == 'n':
    mdistance=((float(input("How many kilometers did you drive?"))))
    mfuel=((float(input("How many liters of gas did you use?"))))
#We will now calculate the Liters/100km and the equal USC units
    mcm=mfuel/mdistance*100
    distance=mdistance*0.621371
    fuel=mfuel*0.264172
    mpg=distance/fuel
#We will now present the user with their statistics in both USC and Metric
    print('                     \tUSC                 \tMetric         ')
    print('Distance___________: \t{:.3f} miles\t{:.3f} Km'.format(distance, mdistance))
    print('Gas________________: \t{:.3f} gallons\t{:.3f} Liters'.format(fuel, mfuel))
    print('Consumption________: \t{:.3f} mpg\t{:.3f} 1/100Km'.format(mpg, mcm))
#Now using the guidlines provided we can give the user a gas consumption rating
    if mcm >20: print('Gas Consumption Rating:Extremely poor')
    elif 15< mcm <=20: print('Gas Consumption Rating:Poor')
    elif 10< mcm <=15: print('Gas Consumption Rating:Average')
    elif 8< mcm <=10: print('Gas Consumption Rating:Good')
    elif mcm <=8: print('Gas Consumption Rating:Excellent')







