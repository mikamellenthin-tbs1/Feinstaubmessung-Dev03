import mysql.connector
# colorama_demo.py
from colorama import init, Fore
# Initializes Colorama
init(autoreset=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sensordb"
)

datum = input('geben sie ein Datum ein: ')

def Max_Min_AVG_Weather(datum):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(temperature),MIN(temperature),AVG(temperature),MAX(humidity),MIN(humidity),AVG(humidity) FROM weather WHERE CAST(timestamp AS DATE)= '%s';" % datum)
    result = mycursor.fetchall()

    for row in result:
        print('Max temperature ' + Fore.RED + str(row[0]))
        print('Min temperature ' + Fore.RED + str(row[1]))
        print('Durchschnitt temperature ' + Fore.RED + str(row[2]))
        print('------------------------------------------')
        print('Max Humidity ' + Fore.RED + str(row[3]))
        print('Min Humidity ' + Fore.RED + str(row[4]))
        print('Durchschnitt Humidity ' + Fore.RED + str(row[5]))
        print('------------------------------------------')

def Max_Min_AVG_Feinstaub(datum):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(P1),MIN(P1),AVG(P1) FROM Feinstaub WHERE CAST(timestamp AS DATE)= '%s';" % datum)
    result = mycursor.fetchall()

    for row in result:
        print('Max Feinstaub ' + Fore.RED + str(row[0]))
        print('Min Feinstaub ' + Fore.RED + str(row[1]))
        print('Durchschnitt Feinstaub ' + Fore.RED + str(row[2]))

Max_Min_AVG_Weather(datum)
Max_Min_AVG_Feinstaub(datum)

mydb.close()

