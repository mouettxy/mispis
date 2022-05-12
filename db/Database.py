import sqlite3
from sqlite3 import Error
import pyodbc

class Config:
  server = 'localhost\sqlexpress' 
  database = 'MISPIS' 
  username = '' 
  password = '' 

class Database:
  def __init__(self):
    self.connect()

  def __del__(self):
    self.disconnect()

  def connect(self):

    try:
      self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Config.server+';DATABASE='+Config.database+';UID='+Config.username+';PWD='+ Config.password)

      print("Connection to SQL Server successful")
    except Error as e:
      print(f"The error '{e}' occurred")
      
  def disconnect(self):
    try:
      self.connection.close()
      print("Closed connection to SQL Server")
    except Error as e:
      print(f"The error '{e}' occurred")

  def execute(self, query):
    try:
      cursor = self.connection.cursor()

      cursor.execute(query)

      return cursor.fetchall()
    except pyodbc.ProgrammingError as e:
      print(f"The error '{e}' occurred")
      return None

  def query(self, query: str):
    try:
      cursor = self.connection.cursor()

      cursor.execute(query)

      cursor.commit()

      return cursor.fetchall()
    except pyodbc.ProgrammingError as e:
      print(f"The error '{e}' occurred")
      return None

  def init(self):
    cursor = self.connection.cursor()

    cursor.execute('''
      SET NOCOUNT ON;
      IF OBJECT_ID(N'dbo.users', N'U') IS NULL
      BEGIN
        CREATE TABLE users (
          id int IDENTITY(1,1), 
          credentials varchar(255), email varchar(255),
          PRIMARY KEY (id)
        )
      END;
    ''')

    cursor.execute('''
      SET NOCOUNT ON;
      IF OBJECT_ID(N'dbo.services', N'U') IS NULL
      BEGIN 
        CREATE TABLE services (
          id int IDENTITY(1,1),
          title varchar(255),
          status int,
          url varchar(255),
          user_id int,
          PRIMARY KEY (id),
          FOREIGN KEY (user_id) REFERENCES users(id)
        )
      END;
    ''')

    cursor.execute('''
      SET NOCOUNT ON;
      IF OBJECT_ID(N'dbo.announcements', N'U') IS NULL
      BEGIN 
        CREATE TABLE announcements (
          id int IDENTITY(1,1),
          title varchar(255),
          description varchar(255),
          user_id int,
          created_at DATETIME,
          PRIMARY KEY (id),
          FOREIGN KEY (user_id) REFERENCES users(id)
        )
      END;
    ''')

    cursor.commit()
  
  def populate(self):
    cursor = self.connection.cursor()

    cursor.execute('''
      INSERT INTO 
        users (credentials, email)
      VALUES 
        ('admin', 'lis@chaikovskie.com'),
        ('user1', 'user1@gmail.com'),
        ('user2', 'user2@gmail.com'),
        ('user3', 'user3@gmail.com')
    ''')

    cursor.commit()

    cursor.execute('''
      INSERT INTO 
        services (title, status, url, user_id)
      VALUES 
        ('Google', 200, 'http://www.google.com', 9),
        ('Yandex', 200, 'http://yandex.ru', 9),
        ('Openscience', 200, 'https://sve.openscience.academy/', 9)
    ''')

    cursor.commit()

    cursor.execute('''
      INSERT INTO 
        announcements (title, description, user_id, created_at)
      VALUES 
        ('Проишествие 1', 'Что-то ужасное', 9, '2020-01-01'),
        ('Проишествие 2', 'Что-то не очень ужасное', 9, '2020-01-02'),
        ('Проишествие 3', 'В целом всё терпимо', 9, '2020-01-03')
    ''')

    cursor.commit()
