"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query, create, update, delete

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Perform CURD operations...")
query()

# Create new entry
create("Test Airline", 5000000, 2, 1, 100, 3, 1, 150)

# Update existing entry
update("Test Airline", 5)

# Delete entry
delete("Test Airline")
