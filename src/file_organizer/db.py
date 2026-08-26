import sqlite3
import contextlib 

DB_PATH = "file_organizer.db"

def create_database():
	with contextlib.closing(sqlite3.connect(DB_PATH)) as conn:
		with conn:
			conn.executescript("""CREATE TABLE IF NOT EXISTS templates( 
								id integer PRIMARY KEY, 
								name TEXT UNIQUE NOT NULL);
							
							CREATE TABLE temp_rules(
							id integer PRIMARY KEY,
							template_id integer NOT NULL,
							extension TEXT NOT NULL,
							destination TEXT NOT NULL,
							FOREIGN KEY (template_id) REFERENCES templates(id));
							""")
	print("Database and tables created successfully.")


def insert_template(name):
    with contextlib.closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO templates (name) VALUES (?)", (name,))
    return cursor.lastrowid

def insert_temp_rule(template_id, extension, destination):
    with contextlib.closing(sqlite3.connect(DB_PATH)) as conn:
          with conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO temp_rules (template_id, extension, destination) VALUES (?, ?, ?)", (template_id, extension, destination))

def get_template_names():
    with contextlib.closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM templates")
        return cursor.fetchall()

def get_template(template_name):
    with contextlib.closing(sqlite3.connect(DB_PATH)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM templates WHERE name = ?", (template_name,))
        template_id = cursor.fetchone()
        if template_id:
            cursor.execute("SELECT extension, destination FROM temp_rules WHERE template_id = ?", (template_id[0],))
            return dict(cursor.fetchall())
        else:
            return None 