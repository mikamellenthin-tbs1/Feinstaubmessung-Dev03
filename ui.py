# Import the required libraries
import mysql.connector
from tkinter import FALSE, Label, ttk
import tkinter as tk
from tkcalendar import Calendar,DateEntry

root = tk.Tk()
root.title('Sensor location')
root.geometry("700x500")
temperatur = tk.StringVar()
humidity = tk.StringVar()
durchschnittlich = tk.StringVar()


def Filter(date):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sensordb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("select MIN(temperature),MAX(humidity) ,AVG(temperature) FROM weather WHERE TIMESTAMP= '%s';" % date)
    result = mycursor.fetchall()

    for row in result:
        temperatur.set(str(row[0]))
        humidity.set(str(row[1]))
        durchschnittlich.set(int(row[2]))
    mydb.close()

def Display():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sensordb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select id,sensor_id,timestamp,temperature,humidity from weather limit 100")
    result = mycursor.fetchall()

    for row in result:
        tree.insert("", tk.END, values=row)        
        mydb.close()

# Create a Groupbox
groupbox = tk.LabelFrame(root, text="Filter Sensor Data")

# Create a Label inside the Groupbox
label = tk.Label(groupbox, text="Enter or select a date :")
label.grid(row=0,column=0,padx=10, pady=10)

# Create a Datepicker inside the Groupbox
datepicker = DateEntry(groupbox)
datepicker.grid(row=0,column=1,padx=10, pady=10)


button1 = tk.Button(groupbox, text="Suche",command=lambda: Filter(datepicker.get()))
button1.grid(row=0,column=2,padx=10, pady=10)

button1 = tk.Button(groupbox, text="Display Data",command=Display)
button1.grid(row=0,column=3,padx=10, pady=10)

# Create a Label inside the Groupbox
label1 = tk.Label(groupbox, text="Max Temperatur :")
label1.grid(row=1,column=0,padx=10, pady=10)

# Create a Label inside the Groupbox
label_temperatur_result = tk.Label(groupbox, text="0", textvariable=temperatur)
label_temperatur_result.grid(row=1,column=1)

# Create a Label inside the Groupbox
label2 = tk.Label(groupbox, text="Max Humidity :")
label2.grid(row=2,column=0,padx=10, pady=10)

# Create a Label inside the Groupbox
label_humidity_result = tk.Label(groupbox, text="0", textvariable=humidity)
label_humidity_result.grid(row=2,column=1,padx=10, pady=10)

# Create a Label inside the Groupbox
label3 = tk.Label(groupbox, text="0", textvariable=durchschnittlich)
label3.grid(row=3,column=1,padx=10, pady=10)

# Create a Label inside the Groupbox
label_Durchschnittlich = tk.Label(groupbox, text="Durchschnittlich :")
label_Durchschnittlich.grid(row=3,column=0,padx=10, pady=10)

# Add the Groupbox to the root window
groupbox.pack(side="top", anchor="nw",padx=10, pady=10)

# Create a GroupBox container
groupbox1 = tk.LabelFrame(root, text="Sensor Data")
groupbox1.pack(fill='both', expand=True, padx=10)

tree = ttk.Treeview(groupbox1, column=("c1", "c2", "c3","c2","c3"), show='headings')

tree.column("#1", anchor=tk.CENTER,width=40)
tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER,width=40)
tree.heading("#2", text="SENSOR_ID")

tree.column("#3", anchor=tk.CENTER,width=40)
tree.heading("#3", text="TIMESTAMP")

tree.column("#4", anchor=tk.CENTER,width=40)
tree.heading("#4", text="TEMPERATUR")

tree.column("#5", anchor=tk.CENTER,width=40)
tree.heading("#5", text="HUMIDITY")

# Create a scrollbar and attach it to the Treeview
scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Pack the Treeview and scrollbar into the root window
scrollbar.pack(side="right", fill="y")
tree.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()