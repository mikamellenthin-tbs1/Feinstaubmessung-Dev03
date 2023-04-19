import os
import csv
import mysql.connector
import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sensordb"
)

mycursor = mydb.cursor()

# Iterate over the files in the folder
folder_path = 'C:/Users/k.bousaid/Desktop/Feinstaubmessung-Dev03/weather'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Read the data from the CSV file
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row
            for row in csvreader:
                for i in row:

                    sql = "INSERT INTO weather (sensor_id, timestamp, temperature,humidity) VALUES (%s, %s, %s, %s)"
                    value = (i.split(';')[0],i.split(';')[5],i.split(';')[6],i.split(';')[7])
                    mycursor.execute(sql, value)
                    mydb.commit()