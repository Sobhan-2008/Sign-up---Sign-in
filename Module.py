import sqlite3

class Database:
    def __init__(self, db_path):
  
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
    
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS login(
                id INTEGER PRIMARY KEY,
                fname TEXT,
                lname TEXT,
                email TEXT,
                password TEXT
            )
        ''')
        self.con.commit()

    def insert(self, fname, lname, email, password):

        self.cur.execute('INSERT INTO login (fname, lname, email, password) VALUES (?, ?, ?, ?)', 
                         (fname, lname, email, password))
        self.con.commit()

    def fetch(self, email, password):
  
        self.cur.execute('SELECT * FROM login WHERE email = ? AND password = ?', (email, password))
        return self.cur.fetchall()

    def close(self):
   
        self.con.close()
