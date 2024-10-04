"""Query the database"""

import sqlite3


def query(db_name="AirlineDB.db"):
    """Query the database for the rows of the AirlineDB table"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AirlineDB")
    rows = cursor.fetchall()
    conn.close()
    return rows


def create(
    airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99,
    fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14,
    db_name="AirlineDB.db"
):
    """Insert a new row into the AirlineDB table"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO AirlineDB (
            airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, 
            fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99,
            fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14
        )
    )
    conn.commit()
    conn.close()
    return f"Inserted airline: {airline}"


def update(airline, new_incidents_00_14, db_name="AirlineDB.db"):
    """Update the number of incidents from 2000-2014 for a specific airline"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE AirlineDB 
        SET incidents_00_14 = ?
        WHERE airline = ?
        """,
        (new_incidents_00_14, airline)
    )
    conn.commit()
    conn.close()
    return f"Updated airline: {airline} with incidents_00_14 = {new_incidents_00_14}"


def delete(airline, db_name="AirlineDB.db"):
    """Delete a specific airline from the AirlineDB table"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM AirlineDB 
        WHERE airline = ?
        """,
        (airline,)
    )
    conn.commit()
    conn.close()
    return f"Deleted airline: {airline}"
