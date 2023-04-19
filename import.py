#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#imports
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
import csv, os, glob, math
import datetime
import sqlite3
#from dateutil.parser import parse

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#config
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

csPathSourceData = "**/Quelldaten"

csPathDB = "**/particulate_matter_measurement.db"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#global variables
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

aFileDataSensor_Location            = []
aFileDataWeather                    = []
aFileDataParticulate_matter         = []
LastIDWeather                       = 0
LastIDParticulate_matter            = 0

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#global constants
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
csSQLSensor_Location              = "INSERT INTO Sensor_Location (Sensor_ID, Sensor_Type, Location, Latitue, Longitude) values(?, ?, ?, ?, ?)"
csSQLWeather                      = "INSERT INTO Weather (ID, Sensor_ID, Timestamp, Humidity, Temperature) values(?, ?, ?, ?, ?)"
csSQLparticulate_matter           = "INSERT INTO particulate_matter (ID, Sensor_ID, Timestamp, P1, Dur_P1, Ratio_P1, P2, Dur_P2, Ratio_P2) values(?, ?, ?, ?, ?, ?, ?, ?, ?)"

csColumnNamesWeather                    = "sensor_id;sensor_type;location;lat;lon;timestamp;temperature;humidity"
csColumnNamesParticulate_matter         = "sensor_id;sensor_type;location;lat;lon;timestamp;P1;durP1;ratioP1;P2;durP2;ratioP2"

oConnection                             = sqlite3.connect(csPathDB)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#functions
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

#csv reader
def initialize(folder_path):
    global aFileDataSensor_Location 
    global aFileDataWeather
    global aFileDataParticulate_matter
    
    #iterate through csv files
    i = 0
    for filename in glob.glob(os.path.join(folder_path, '*.csv')):
        aFileDataSensor_Location    = []
        aFileDataWeather            = []
        aFileDataParticulate_matter = []

        with open(filename, 'r') as csvfile:

            #get the data for one csv file
            csvFileData = csv.reader(csvfile, delimiter=';')
            j = 0
            sColumnNames = ""
            for row in csvFileData:
                #Get the Columns names for the current file
                if j==0:
                    sColumnNames = ";".join(row)
                else:
                    updateDataArrays(row, sColumnNames)
                j = j + 1
            updateTable_Sensor_Location(aFileDataSensor_Location)
            upDateTables()
        i = i + 1
    
    
    print("number of files: " + str(i))



def updateTable_Sensor_Location(aFileDataSensor_Location  ):
    #open connection to database
    with oConnection:     

        #iterate all the tuples from aFileDataSensor_Location  
        for DataTuple in aFileDataSensor_Location:
            #get sensor id of current tuple
            SensorID = DataTuple[0]
            SensorIdIsTaken = False

            #check if sensor id of the current tuple is already taken in table Sensor_Location
            response = oConnection.execute("SELECT * FROM Sensor_Location")
            for row in response:
                if SensorID == row [0]:
                    SensorIdIsTaken = True
                    break
            if SensorIdIsTaken == True:
                break
            else:
                aSQLData = [(DataTuple)]
                oConnection.executemany(csSQLSensor_Location, aSQLData)


def upDateTables():

    #open connection to database
    with oConnection:
        oConnection.executemany(csSQLWeather, aFileDataWeather)
        oConnection.executemany(csSQLparticulate_matter, aFileDataParticulate_matter)

            


def updateDataArrays(row, sColumnNames):
    global LastIDWeather
    global LastIDParticulate_matter 

    entryTuple = []
    # biuld new tupels for sensor type
    i = 0
    for entry in row:
        #check the type of the entry
        if i == 0:
            entry = int(entry)
            entryTuple.append(entry)
        elif i == 1:
            entry = str(entry)
            entryTuple.append(entry)
        elif i == 2:
            entry = float(entry)
            entryTuple.append(entry)
        elif i == 3:
            entry = float(entry)
            entryTuple.append(entry)
        elif i == 4:
            entry = float(entry)
            entryTuple.append(entry)                    
        i = i + 1
    entryTuple = tuple(entryTuple)
    aFileDataSensor_Location.append(entryTuple)



    if sColumnNames == csColumnNamesWeather:
        entryTuple = []
        entryTuple.append(LastIDWeather)
        LastIDWeather = LastIDWeather + 1
        # biuld new tupels for Weather
        i = 0
        for entry in row:
            if i == 0:
                entry = int(entry)
                entryTuple.append(entry)
            elif i == 5:
                entry = datetime.datetime.strptime(entry, "%Y-%m-%dT%H:%M:%S")
                entryTuple.append(entry)
            elif i == 6:
                entry = float(entry)
                entryTuple.append(entry)
            elif i == 7:
                entry = float(entry)
                entryTuple.append(entry)
            i = i + 1

        entryTuple = tuple(entryTuple)
        aFileDataWeather.append(entryTuple)           


    if sColumnNames == csColumnNamesParticulate_matter:
        entryTuple = []
        entryTuple.append(LastIDParticulate_matter)
        LastIDParticulate_matter = LastIDParticulate_matter + 1
        # biuld new tupels for Particulate_matter
        i = 0
        for entry in row:
            if i == 0:
                entry = int(entry)
                entryTuple.append(entry)
            elif i == 5:
                entry = datetime.datetime.strptime(entry, "%Y-%m-%dT%H:%M:%S")
                entryTuple.append(entry)
            elif i == 6:
                entry = float(entry)
                entryTuple.append(entry)
            elif i == 7:
                if entry == "":
                    entry = 0.00
                entry = float(entry)
                entryTuple.append(entry)
            elif i == 8:
                if entry == "":
                    entry = 0.00
                entry = float(entry)
                entryTuple.append(entry)
            elif i == 9:
                entry = float(entry)
                entryTuple.append(entry)
            elif i == 10:
                if entry == "":
                    entry = 0.00
                entry = float(entry)
                entryTuple.append(entry)
            elif i == 11:
                if entry == "":
                    entry = 0.00
                entry = float(entry)
                entryTuple.append(entry)
            i = i + 1
        
        entryTuple = tuple(entryTuple)
        aFileDataParticulate_matter.append(entryTuple)
        

#sensor_id;sensor_type;location;lat;lon;timestamp;P1;durP1;ratioP1;P2;durP2;ratioP2
# CREATE TABLE particulate_matter(
# 	ID INT NOT NULL,            
# 	Sensor_ID INT NOT NULL,         0 
# 	Timestamp DATETIME,             5 
# 	P1 DOUBLE,                      6
# 	Dur_P1 DOUBLE,                  7
# 	Ratio_P1 DOUBLE,                8
# 	P2 DOUBLE,                      9
# 	Dur_P2 DOUBLE,                  10
# 	Ratio_P2 DOUBLE,                11
# 	PRIMARY KEY(ID),
# 	FOREIGN KEY (Sensor_ID) REFERENCES Sensor_Location (Sensor_ID)	
# );


def GetLastIDFromTable(TableName):
    iResult = 0
    sql = "SELECT * FROM " + TableName
    with oConnection:
        response = oConnection.execute(sql)
        iResult = len(response.fetchall())
    return iResult


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#initialize
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
LastIDWeather = GetLastIDFromTable("Weather")
LastIDParticulate_matter = GetLastIDFromTable("particulate_matter")
# print("LastIDWeather: " + str(LastIDWeather))
# print("LastIDParticulate_matter: " + str(LastIDParticulate_matter))
initialize(csPathSourceData)











