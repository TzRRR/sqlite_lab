import pytest
import sqlite3
from main import query, create, update, delete

# Define a test database name for isolation
TEST_DB = "TestAirlineDB.db"


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Setup and teardown for the test database"""
    # Set up: Create a test database and initialize the table
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS AirlineDB")
    cursor.execute(
        """
        CREATE TABLE AirlineDB (
            airline TEXT,
            avail_seat_km_per_week INTEGER,
            incidents_85_99 INTEGER,
            fatal_accidents_85_99 INTEGER,
            fatalities_85_99 INTEGER,
            incidents_00_14 INTEGER,
            fatal_accidents_00_14 INTEGER,
            fatalities_00_14 INTEGER
        )
    """
    )
    # Insert initial test data
    cursor.executemany(
        """
        INSERT INTO AirlineDB VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        [
            ("Airline A", 1000000, 2, 0, 0, 1, 0, 0),
            ("Airline B", 2000000, 3, 1, 50, 2, 1, 100),
        ],
    )
    conn.commit()
    conn.close()

    # Yield control to tests
    yield

    # Teardown: Remove the test database file
    # import os
    # os.remove(TEST_DB)


def test_query():
    """Test querying all rows from the database"""
    result = query(db_name=TEST_DB)
    assert len(result) == 2, "Query did not return the correct number of rows"
    assert result[0][0] == "Airline A", "First airline name does not match expected"


def test_create():
    """Test inserting a new row into the database"""
    create("Airline C", 3000000, 4, 1, 20, 2, 1, 50, db_name=TEST_DB)
    result = query(db_name=TEST_DB)
    assert len(result) == 3, "Create did not add a new row"
    assert result[2][0] == "Airline C", "New airline name does not match expected"


def test_update():
    """Test updating an existing row in the database"""
    update("Airline A", 5, db_name=TEST_DB)
    result = query(db_name=TEST_DB)
    updated_row = next(row for row in result if row[0] == "Airline A")
    assert (
        updated_row[5] == 5
    ), "Update did not change the incidents_00_14 value correctly"


def test_delete():
    """Test deleting a row from the database"""
    delete("Airline B", db_name=TEST_DB)
    result = query(db_name=TEST_DB)
    assert len(result) == 2, "Delete did not remove the row correctly"
    assert not any(
        row[0] == "Airline B" for row in result
    ), "Deleted airline still found in the table"
