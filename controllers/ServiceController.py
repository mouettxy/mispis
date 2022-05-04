from db.Database import Database

class ServiceController:
  def __init__(self, DB: Database):
    self.DB = DB

  def get_all(self):
    return self.DB.query('''
      SELECT * FROM services
      INNER JOIN users ON users.id = services.user_id
    ''')

  def get_by_id(self, id: int):
    return self.DB.query(f'''
      SELECT * FROM services WHERE id = {id}
      INNER JOIN users ON users.id = services.user_id
    ''')
