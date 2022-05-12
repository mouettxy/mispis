from db.Database import Database

class UserController:
  def __init__(self, DB: Database):
    self.DB = DB
  
  def get_all(self):
    return self.DB.execute('''
      SELECT * FROM users
    ''')
  
  def get_by_id(self, id: int):
    return self.DB.execute(f'''
      SELECT * FROM users WHERE id = {id}
    ''')
