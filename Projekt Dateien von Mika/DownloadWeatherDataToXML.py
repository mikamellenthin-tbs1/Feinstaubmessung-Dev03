import sqlite3
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

print('-> START <-');

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('particulate_matter_measurement.db')
cursor = conn.cursor()
print('-> Connection success');

# SQL-Abfrage ausführen, um alle Daten aus der Tabelle "Weather" abzurufen
cursor.execute("SELECT * FROM Weather")
rows = cursor.fetchall()
print('-> Collect data from DB');

# XML-Struktur erstellen
root = ET.Element("WeatherData")
print('-> Create XML-File');

# Für jeden Datensatz in der Datenbank einen XML-Knoten erstellen
for row in rows:
    weather_entry = ET.SubElement(root, "WeatherEntry")
    
    id_element = ET.SubElement(weather_entry, "ID")
    id_element.text = str(row[0])
    
    sensor_id_element = ET.SubElement(weather_entry, "Sensor_ID")
    sensor_id_element.text = str(row[1])
    
    timestamp_element = ET.SubElement(weather_entry, "Timestamp")
    timestamp_element.text = row[2]
    
    temperature_element = ET.SubElement(weather_entry, "Temperature")
    temperature_element.text = str(row[3])
    
    humidity_element = ET.SubElement(weather_entry, "Humidity")
    humidity_element.text = str(row[4])

# XML-Dokument erstellen
tree = ET.ElementTree(root)

# XML-Dokument in eine Datei exportieren und formatieren
tree.write("weather_data.xml", encoding="utf-8", xml_declaration=True)
dom = minidom.parse("weather_data.xml")
with open("weather_data.xml", "w", encoding="utf-8") as file:
    file.write(dom.toprettyxml(indent="  "))

print('-> XML-File ready');

# Verbindung zur SQLite-Datenbank schließen
conn.close()
print('-> Connection closed');

print('-> EXIT <-');