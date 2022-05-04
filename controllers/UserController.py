from db.Database import Database

class UserController:
  def __init__(self, DB: Database):
    self.DB = DB
  
  def get_all(self):
    return self.DB.query('''
      SELECT * FROM users
    ''')
  
  def get_by_id(self, id: int):
    return self.DB.query(f'''
      SELECT * FROM users WHERE id = {id}
    ''')
