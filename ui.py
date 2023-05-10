# Import the required libraries
import mysql.connector
from tkinter import FALSE, Label, ttk
import tkinter as tk
from tkcalendar import Calendar,DateEntry

root = tk.Tk()
root.title('Sensor location')
root.geometry("700x500")
max_temperatur_value = tk.IntVar()
min_temperatur_value = tk.IntVar()
avg_temperatur_value = tk.IntVar()
max_humidity_value = tk.IntVar()
min_humidity_value = tk.IntVar()
avg_humidity_value = tk.IntVar()
max_feinstaub_value = tk.IntVar()
min_feinstaub_value = tk.IntVar()
avg_feinstaub_value = tk.IntVar()


def Max_Min_AVG_Weather(date):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sensordb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(temperature),MIN(temperature),AVG(temperature),MAX(humidity),MIN(humidity),AVG(humidity) FROM weather WHERE CAST(timestamp AS DATE) = '%s';" % date)
    result = mycursor.fetchall()

    for row in result:
        if(row[0] == None or row[1] == None or row[2] == None or row[3] == None or row[4] == None or row[5] == None):
            print('Now data Avialable for this date or date format not correct')
        else:
            max_temperatur_value.set(float('{:.2f}'.format(row[0])))
            min_temperatur_value.set(float('{:.2f}'.format(row[1])))
            avg_temperatur_value.set(float('{:.2f}'.format(row[2])))
            max_humidity_value.set(float('{:.2f}'.format(row[3])))
            min_humidity_value.set(float('{:.2f}'.format(row[4])))
            avg_humidity_value.set(float('{:.2f}'.format(row[5])))
            Max_Min_AVG_Feinstaub(date)
    mydb.close()

def Max_Min_AVG_Feinstaub(date):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sensordb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(P1),MIN(P1),AVG(P1) FROM Feinstaub WHERE CAST(timestamp AS DATE)= '%s';" % date)
    result = mycursor.fetchall()

    for row in result:
        if(row[0] == None or row[1] == None or row[2] == None):
            print('Now data Avialable for this date or date format not correct')
        else:
            print(row.count)
            max_feinstaub_value.set(float('{:.2f}'.format(row[0])))
            min_feinstaub_value.set(float('{:.2f}'.format(row[1])))
            avg_feinstaub_value.set(float('{:.2f}'.format(row[2])))
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
    mycursor.execute("select id,sensor_id,timestamp,temperature,humidity from weather")
    result = mycursor.fetchall()

    for row in result:
        tree.insert("", tk.END, values=row)        
        mydb.close()

# Create a Groupbox_1
groupbox_filter = tk.LabelFrame(root, text="Filter Sensor Data")

# Create a Label inside the Groupbox
label = tk.Label(groupbox_filter, text="Enter or select a date :")
label.grid(row=0,column=0,padx=10, pady=10)

# Create a Datepicker inside the Groupbox
datepicker = DateEntry(groupbox_filter, date_pattern="yyyy-mm-dd")
datepicker.grid(row=0,column=1,padx=10, pady=10)

button1 = tk.Button(groupbox_filter, text="Suche",command=lambda: Max_Min_AVG_Weather(datepicker.get()))
button1.grid(row=0,column=2,padx=10, pady=10)

button1 = tk.Button(groupbox_filter, text="Display Data",command=Display)
button1.grid(row=0,column=3,padx=10, pady=10)

# Add the Groupbox to the root window
groupbox_filter.pack(side="top",fill="both",padx=10, pady=10)

# Create a Groupbox_1
groupbox = tk.LabelFrame(root, text="Bewertung von daten")

# Data Max,Min,AVG temperatur
label_max_temperatur = tk.Label(groupbox, text="Max temperatur:")
label_max_temperatur.grid(row=1,column=0,padx=10, pady=10)

label_max_temperatur_result = tk.Label(groupbox,fg='red', text="0", textvariable=max_temperatur_value)
label_max_temperatur_result.grid(row=1,column=1,padx=10, pady=10)

label_min_temperatur = tk.Label(groupbox, text="Min temperatur:")
label_min_temperatur.grid(row=2,column=0,padx=10, pady=10)

label_max_temperatur_result = tk.Label(groupbox,fg='red', text="0", textvariable=min_temperatur_value)
label_max_temperatur_result.grid(row=2,column=1,padx=10, pady=10)

label_avg_temperatur = tk.Label(groupbox, text="AVG temperatur:")
label_avg_temperatur.grid(row=3,column=0,padx=10, pady=10)

label_avg_temperatur_result = tk.Label(groupbox,fg='red', text="0", textvariable=avg_temperatur_value)
label_avg_temperatur_result.grid(row=3,column=1)

# Data Max,Min,AVG Humidity
label_max_humidity = tk.Label(groupbox, text="Max Humidity:")
label_max_humidity.grid(row=1,column=3,padx=10, pady=10)

label_max_humidity_result = tk.Label(groupbox,fg='red', text="0", textvariable=max_humidity_value)
label_max_humidity_result.grid(row=1,column=4,padx=10, pady=10)

label_min_humidity = tk.Label(groupbox, text="Min Humidity:")
label_min_humidity.grid(row=2,column=3,padx=10, pady=10)

label_min_humidity_result = tk.Label(groupbox, fg='red',text="0", textvariable=min_humidity_value)
label_min_humidity_result.grid(row=2,column=4,padx=10, pady=10)

label_avg_humidity = tk.Label(groupbox, text="AVG Humidity:")
label_avg_humidity.grid(row=3,column=3,padx=10, pady=10)

label_avg_humidity_result = tk.Label(groupbox,fg='red', text="0", textvariable=avg_humidity_value)
label_avg_humidity_result.grid(row=3,column=4,padx=10, pady=10)

# Data Max,Min,AVG Feinstaub
label_max_feinstaub = tk.Label(groupbox, text="Max Feinstaub:")
label_max_feinstaub.grid(row=1,column=5,padx=10, pady=10)

# Create a Label inside the Groupbox
label_max_feinstaub_result = tk.Label(groupbox,fg='red', text="0", textvariable=max_feinstaub_value)
label_max_feinstaub_result.grid(row=1,column=6)

label_min_feinstaub = tk.Label(groupbox, text="Min Feinstaub:")
label_min_feinstaub.grid(row=2,column=5,padx=10, pady=10)

min_feinstaub_result = tk.Label(groupbox,fg='red', text="0", textvariable=min_feinstaub_value)
min_feinstaub_result.grid(row=2,column=6,padx=10, pady=10)

label_avg_feinstaub = tk.Label(groupbox, text="AVG Feinstaub:")
label_avg_feinstaub.grid(row=3,column=5,padx=10, pady=10)

label_avg_feinstaub_result = tk.Label(groupbox,fg='red', text="0", textvariable=min_feinstaub_value)
label_avg_feinstaub_result.grid(row=3,column=6,padx=10, pady=10)

# Add the Groupbox to the root window
groupbox.pack(side="top",fill="both",padx=10, pady=10)

# Create a GroupBox Treeview
groupbox_Sensor_Data = tk.LabelFrame(root, text="Sensor Data")

tree = ttk.Treeview(groupbox_Sensor_Data, column=("c1", "c2", "c3","c2","c3"), show='headings')

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

groupbox_Sensor_Data.pack(fill="both", expand=True,padx=10,pady=10)

root.mainloop()