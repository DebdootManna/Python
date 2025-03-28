import sqlite3

def main():
    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        print("Connected to SQLite database!")

        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        age INTEGER)''')
        
        cursor.execute("INSERT INTO students (name, age) VALUES ('Debdoot', 20)")
        cursor.execute("INSERT INTO students (name, age) VALUES ('Ananya', 20)")
        conn.commit()
        print("Inserted 2 records")

        cursor.execute("SELECT * FROM students")
        all_rows = cursor.fetchall()
        print("\nAll records:")
        for row in all_rows:
            print(row)

        cursor.execute("SELECT * FROM students")
        print("\nFirst record:", cursor.fetchone())

        cursor.execute("UPDATE students SET age = 21 WHERE name = 'Debdoot'")
        conn.commit()
        print("\nUpdated Debdoot's age")

        cursor.execute("DELETE FROM students WHERE name = 'Ananya'")
        conn.commit()
        print("Deleted Ananya's record")

        cursor.execute("SELECT * FROM students")
        some_rows = cursor.fetchmany(1)
        print("\nFirst record using fetchmany:", some_rows)

    except sqlite3.Error as error:
        print("SQLite error:", error)
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed")

if __name__ == "__main__":
    main()