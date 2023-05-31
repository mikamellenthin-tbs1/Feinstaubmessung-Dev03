import os
import sqlite3
import csv

# Verzeichnis mit CSV-Dateien
directory = input("Bitte geben Sie den Pfad zum Verzeichnis mit den CSV-Dateien ein: ")

# Name der SQLite-Datenbank
db_name = "particulate_matter.db"

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Tabelle "Sensor" erstellen, wenn sie noch nicht existiert
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sensor (
        ID INTEGER PRIMARY KEY,
        location NUMERIC,
        latitude NUMERIC,
        longitude NUMERIC,
        type TEXT
    )
""")

# Alle CSV-Dateien im Verzeichnis durchgehen
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # CSV-Datei einlesen
        with open(os.path.join(directory, filename), newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            next(reader)  # Überspringe die erste Zeile (Header)

            # Eintrag für jeden Datensatz in der CSV-Datei erstellen
            for row in reader:
                sensor_id = row[0]
                location = row[1]
                latitude = row[2]
                longitude = row[3]
                sensor_type = row[4]
                print(row)

                # SQL-Abfrage zum Einfügen des Eintrags erstellen und ausführen
                sql_query = f"""
                    INSERT INTO Sensor (ID, location, latitude, longitude, type)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(sql_query, (sensor_id, location, latitude, longitude, sensor_type))

# Änderungen in der Datenbank speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank-Update abgeschlossen.")
