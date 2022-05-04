import sqlite3
from sqlite3 import Error

class Database:
  def __init__(self):
    self.connect()
    self.init()

  def __del__(self):
    self.disconnect()

  def connect(self):
    try:
      self.connection = sqlite3.connect('monitoring.db')
      self.connection.row_factory = sqlite3.Row
      print("Connection to SQLite DB successful")
    except Error as e:
      print(f"The error '{e}' occurred")
      
  def disconnect(self):
    try:
      self.connection.close()
      print("Closed connection to SQLite DB")
    except Error as e:
      print(f"The error '{e}' occurred")

  def query(self, query: str):
    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      self.connection.commit()
      return cursor.fetchall()
    except Error as e:
      print(f"The error '{e}' occurred")
      print(query)
      return None

  def init(self):
    self.query('''
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        credentials TEXT, email TEXT
      )
    ''')

    self.query('''
      CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        status INTEGER,
        url TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
      )
    ''')

    self.query('''
      CREATE TABLE IF NOT EXISTS announcements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        user_id INTEGER,
        created_at DATETIME,
        FOREIGN KEY (user_id) REFERENCES users(id)
      )
    ''')
  
  def populate(self):
    self.query('''
      INSERT INTO 
        users (credentials, email)
      VALUES 
        ('admin', 'lis@chaikovskie.com'),
        ('user1', 'user1@gmail.com'),
        ('user2', 'user2@gmail.com'),
        ('user3', 'user3@gmail.com')
    ''')

    self.query('''
      INSERT INTO 
        services (title, status, url, user_id)
      VALUES 
        ('Google', 200, 'http://www.google.com', 1),
        ('Yandex', 200, 'http://yandex.ru', 1),
        ('Openscience', 200, 'https://sve.openscience.academy/', 1)
    ''')

    self.query('''
      INSERT INTO 
        announcements (title, description, user_id, created_at)
      VALUES 
        ('Проишествие 1', 'Что-то ужасное', 1, '2020-01-01'),
        ('Проишествие 2', 'Что-то не очень ужасное', 1, '2020-01-02'),
        ('Проишествие 3', 'В целом всё терпимо', 1, '2020-01-03')
    ''')
