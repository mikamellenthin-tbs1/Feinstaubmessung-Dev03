import sqlite3
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

print('-> START <-');

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('particulate_matter_measurement.db')
cursor = conn.cursor()
print('-> Connection success');

# SQL-Abfrage ausführen, um alle Daten aus der Tabelle "Weather" abzurufen
cursor.execute("SELECT * FROM 'Sensor_Location'")
rows = cursor.fetchall()
print('-> Collect data from DB');

# XML-Struktur erstellen
root = ET.Element("SensorData")
print('-> Create XML-File');

# Für jeden Datensatz in der Datenbank einen XML-Knoten erstellen
for row in rows:
    sensor_entry = ET.SubElement(root, "SensorEntry")
    
    sensor_id_element = ET.SubElement(sensor_entry, "Sensor_ID")
    sensor_id_element.text = str(row[0])
    
    sensorType_element = ET.SubElement(sensor_entry, "Sensor_Type")
    sensorType_element.text = row[1]
    
    location_element = ET.SubElement(sensor_entry, "Location")
    location_element.text = str(row[2])
    
    latitude_element = ET.SubElement(sensor_entry, "Latitude")
    latitude_element.text = str(row[3])

    longitude_element = ET.SubElement(sensor_entry, "Longitude")
    longitude_element.text = str(row[4])

# XML-Dokument erstellen
tree = ET.ElementTree(root)

# XML-Dokument in eine Datei exportieren und formatieren
tree.write("sensor_data.xml", encoding="utf-8", xml_declaration=True)
dom = minidom.parse("sensor_data.xml")
with open("sensor_data.xml", "w", encoding="utf-8") as file:
    file.write(dom.toprettyxml(indent="  "))

print('-> XML-File ready');

# Verbindung zur SQLite-Datenbank schließen
conn.close()
print('-> Connection closed');

print('-> EXIT <-');