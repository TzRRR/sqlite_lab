# SQLite Lab: CRUD Operations

[![CI](https://github.com/TzRRR/sqlite_lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/TzRRR/sqlite_lab/actions/workflows/cicd.yml)

## Overview

A Python project for performing basic CRUD (Create, Read, Update, Delete) operations on a SQLite database storing airline data.

## Installation

1. **Clone the repository**

   ```bash
   git clone <REPOSITORY_URL>
   cd sqlite_lab
   ```

2. **Set up a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### CRUD Operations

- **Create**: Add a new row to `AirlineDB`.
- **Read**: Fetch rows from `AirlineDB`.
- **Update**: Modify existing rows.
- **Delete**: Remove rows.

Example:

```python
from mylib.query import create, query, update, delete

create("Airline C", 3000000, 4, 1, 20, 2, 1, 50)
print(query())
update("Airline C", 5)
delete("Airline C")
```
