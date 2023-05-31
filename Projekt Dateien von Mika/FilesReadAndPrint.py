import os

# Verzeichnis, in dem sich die CSV-Dateien befinden
directory = "/Users/mika/Programming/data/"

# Schleife durch alle Dateien im Verzeichnis
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Öffnen der CSV-Datei und Ausgabe der Nachricht
        with open(os.path.join(directory, filename), 'r') as file:
            print('Hello World! File:', filename)
