import sqlite3


def read_resource(table_name, db_file='resources/db.db'):
    """Reads all entries from an SQLite table and returns them as a list of dictionaries.

    Args:
        table_name (str): Name of the table.
        db_file (str, optional): Path to the database file. Defaults to 'resources/db.db'.

    Returns:
        List of dictionaries: Each dictionary represents a row with column names as keys.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY Date DESC")
        resources = cursor.fetchall()

    return resources


def read_resource_for_web(section, table_name, db_file='resources/db.db', limit=40):
    """Reads all entries from an SQLite table and returns them as a list of dictionaries.

    Args:
        section(str): Name of section that should be extracted from db.
        table_name (str): Name of the table.
        db_file (str, optional): Path to the database file. Defaults to 'resources/db.db'.
        limit(int): Number of records that should be extracted from db.

    Returns:
        List of dictionaries: Each dictionary represents a row with column names as keys.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE Section='{section}' ORDER BY Date DESC LIMIT '{limit}'")
        resources = cursor.fetchall()

    return resources


def add_entry(entry_data, table_name, db_file='resources/db.db'):
    """Adds a new entry to the specified SQLite table, using parameterization for security.

    Args:
        entry_data (dict): The data to be added as a dictionary.
        table_name (str): Name of the table.
        db_file (str, optional): Path to the database file. Defaults to 'resources/db.db'.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        columns = ', '.join(entry_data.keys())
        placeholders = ', '.join('?' * len(entry_data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(entry_data.values()))
        conn.commit()