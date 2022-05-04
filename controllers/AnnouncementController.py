from db.Database import Database

class AnnouncementController:
  def __init__(self, DB: Database):
    self.DB = DB

  def get_all(self):
    return self.DB.query('''
      SELECT * FROM announcements
      INNER JOIN users ON users.id = announcements.user_id
    ''')

  def get_by_id(self, id: int):
    return self.DB.query(f'''
      SELECT * FROM announcements WHERE id = {id}
      INNER JOIN users ON users.id = announcements.user_id
    ''')