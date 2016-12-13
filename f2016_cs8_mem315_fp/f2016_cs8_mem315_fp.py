#Here we are creating our participation projects
class participant:
    """ participant class"""
    name = "unknown"
    distance = 0
    runs = 0
#Here we are setting up our initializer method
    def __init__(self, name, distance=0):
    #setting the name and initial distance variable for _init_
        self.name = name
        if distance > 0:
            self.distance = distance
            self.runs = 1
#This function allows us to get the name of the participants from our excel file
    def getName(self):
        return self.name
 #Here we are getting our distance variable for the accumulator similiar to getName
    def getDistance(self):
        return self.distance
 #This function adds the distances run for the runners who ran more than once
    #Setting this variable it will be used to the distances accumulator that will be set up
    def getRuns(self):
        return self.runs
 #Here we are setting up the distance accumulator and our single distances
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
 #Here we are setting up the distance accumulator for runners who ran more than
            #once,like addDistance we are adding the variables of distances set up to our distance accumulator
    def addDistances(self, distances):
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
#For this function we are returning a string with our name,distance ran and how
                #many distances/runners who ran more were present
    def __str__(self):
        return \
               #Here we are right aligning our string and setting a limit of20 characters
                #for our name, a limit of 9 digits for total distance and 4 digits for the number of
                #ones
        "Name : " + format(self.name, '>20s') + \
        ". Distance run : " + format(self.distance, '9.4f') + \
        ". Runs : " + format(self.runs, '4d')
    #This function is converting our data to the correct excel format
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
    #Here we are simply extracting the data from our excel document
def getDataFromFile(file):
    output = []
    for line in open(file,'r'):
        if "distance" in line:
            continue
    #Here we are removing the newline character and spliting the two columns of our excel documents
        temp1 = line.rstrip('\n').split(',')
        try:
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            print('Invalid row : '+line.rstrip('\n'))
    return output
#This allows the format of the information derived from the read files in regard to spacing
def printKV(key, value, klen):
    key_length = len(key)
    if klen > key_length:
        key_length = klen
    key = format(key, str(key_length)+'s')
    if isinstance(value, str) == True:
        # #the 30s allows us to take any value that we are printing to truncate whatever amount of spaces we require
        value = format(value, '.20s')
    elif isinstance(value, float) == True:
        value = format(value, '12.5f')
        value = format(str(value), '.30s')
    else:
        value = format(value, '5d')
        value = format(str(value), '.30s')
    print(key+' : '+value)

def main():
    #begin loop
    masterFile = input("Please provide master file : ")
    try:
        dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
    except:
        print("Impossible to read master file or invalid file name")
        exit(1)
    exceldata = sum([getDataFromFile(file) for file in dataFiles],[])
    numberFiles = len(dataFiles)
#Here we set the variable for the total lines and distance that will be displayed when the user quits the program
    totalline = len(exceldata)
    totaldistanceRun = sum([item['distance'] for item in exceldata])
    participants = {}
#Finding if any name has already been read
    for item in exceldata:
        if not item['name'] in participants.keys():
            participants[item['name']] = participant(item['name'])
        participants[item['name']].addDistance(item['distance'])
#setting up the minimum and maximum intervals for our dictionaries
    minDistance = { 'name' : None, 'distance': None }
    maxDistance = { 'name' : None, 'distance': None }
    partcipation = {}
#Finding the actual minimum and maximum distance for our dictionary
    #Finding and setting the new minimum and maximum for our dictionary when they are read
    for name, object in participants.items():
        distance = object.getDistance()
        if minDistance['name'] is None or minDistance['distance'] > distance:
            minDistance['name'] = name
            minDistance['distance'] = distance
        if maxDistance['name'] is None or maxDistance['distance'] < distance:
            maxDistance['name'] = name
            maxDistance['distance'] = distance
        participantAppearences = object.getRuns()
        if not participantAppearences in partcipation.keys():
            partcipation[participantAppearences] = []
        partcipation[participantAppearences].append(name)
#The length of the participants in the dictionary will give us the number of participants
    totalparticipants = len(participants);
    totalmultiplerecordholders = len([1 for item in participants.values() if item.getRuns() > 1])
    INTEGER = '5d'
    FLOAT = '12.5f'
    STRING = '20s'
 #Here we call the functions that display the information read in the file just entered
    printKV('Number of Input files read', numberFiles, 28)
    printKV('Total number of lines read', totalline, 28)
    print('')
    printKV('Total distance run', totaldistanceRun, 28)
    print('')
    printKV('Max distance run', maxDistance['distance'], 28)
    printKV('   by participant', maxDistance['name'], 28)
    print('')
    printKV('Min distance run', minDistance['distance'], 28)
    printKV('   by participant', minDistance['name'], 28)
    print('')
    printKV('Total number of participants', totalparticipants, 28)
    print('Number of participants')
    printKV('   with multiple records', totalmultiplerecordholders, 28)
    print('')
#Here we are convering the data that we read and displayed from our excel documents and creating a file to be outputed
    #with the information once the files have been entered and the data has been displayed
    outputFile = "f2016_cs8_mem315_fp.output.csv"
    fh = open(outputFile,'w')
    fh.write('name,records,distance\n')
    for name, object in participants.items():
        fh.write(object.tocsv() + '\n')
#Close the file to ensure no error
    fh.close()

main()



