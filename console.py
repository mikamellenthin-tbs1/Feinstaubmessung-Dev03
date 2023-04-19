import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sensordb"
)

datum = input('Geben Sie ein gültige datum ein :')

mycursor = mydb.cursor()
mycursor.execute("SELECT MIN(temperature),MAX(humidity) ,AVG(temperature) FROM weather WHERE CAST(timestamp AS DATE)= '%s';" % datum)
result = mycursor.fetchall()

for row in result:
    print('Min temperature ' + str(row[0]))
    print('Max temperature ' + str(row[1]))
    print('Durchschnitt temperature ' + str(row[2]))

mydb.close()