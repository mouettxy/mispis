import mysql.connector

class Database:
  def __init__(self):
    self.connect()

  def __del__(self):
    self.disconnect()

  def connect(self):
    self.connection = mysql.connector.connect(
      user='root', 
      password='rerlopxe1',
      host='127.0.0.1',
      database='mispis'
    )
      
  def disconnect(self):
    self.connection.close()

  def execute(self, query):
    try:
      cursor = self.connection.cursor(dictionary=True)

      cursor.execute(query)

      data = cursor.fetchall()

      self.connection.commit()

      return data
    except:
      return None

  def query(self, query: str):
    try:
      cursor = self.connection.cursor(dictionary=True)

      cursor.execute(query)

      data = cursor.fetchall()

      self.connection.commit()

      return data
    except:
      return None

  def init(self):
    self.execute('''
      CREATE TABLE IF NOT EXISTS users (
        id int AUTO_INCREMENT, 
        credentials varchar(255), email varchar(255),
        PRIMARY KEY (id)
      )
    ''')

    self.execute('''
      CREATE TABLE IF NOT EXISTS services (
        id int AUTO_INCREMENT,
        title varchar(255),
        status int,
        url varchar(255),
        user_id int,
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES users(id)
      )
    ''')

    self.execute('''
      CREATE TABLE IF NOT EXISTS announcements (
        id int AUTO_INCREMENT,
        title varchar(255),
        description varchar(255),
        user_id int,
        created_at DATETIME,
        PRIMARY KEY (id),
        FOREIGN KEY (user_id) REFERENCES users(id)
      )
    ''')
  
  def populate(self):
    self.execute('''
      INSERT INTO 
        users (credentials, email)
      VALUES 
        ('admin', 'lis@chaikovskie.com'),
        ('user1', 'user1@gmail.com'),
        ('user2', 'user2@gmail.com'),
        ('user3', 'user3@gmail.com')
    ''')

    self.execute('''
      INSERT INTO 
        services (title, status, url, user_id)
      VALUES 
        ('Google', 200, 'http://www.google.com', 13),
        ('Yandex', 200, 'http://yandex.ru', 13),
        ('Openscience', 200, 'https://sve.openscience.academy/', 13)
    ''')

    self.execute('''
      INSERT INTO 
        announcements (title, description, user_id, created_at)
      VALUES 
        ('Проишествие 1', 'Что-то ужасное', 13, '2020-01-01'),
        ('Проишествие 2', 'Что-то не очень ужасное', 13, '2020-01-02'),
        ('Проишествие 3', 'В целом всё терпимо', 13, '2020-01-03')
    ''')

