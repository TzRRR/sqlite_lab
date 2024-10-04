"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,
ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="airline.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)
    conn = sqlite3.connect('AirlineDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS AirlineDB")
    c.execute("CREATE TABLE AirlineDB (airline, avail_seat_km_per_week, "
              "incidents_85_99, fatal_accidents_85_99, fatalities_85_99, "
              "incidents_00_14, fatal_accidents_00_14, fatalities_00_14)")
    #insert
    c.executemany("INSERT INTO AirlineDB VALUES (?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "AirlineDB.db"

