from typing_extensions import TypedDict
from db.Database import Database
import requests

class ServiceCreateDto(TypedDict):
  title: str
  url: str

class ServiceUpdateDto(TypedDict):
  id: int
  title: str
  url: str

class ServiceController:
  def __init__(self, DB: Database):
    self.DB = DB

  def get_all(self):
    services = self.DB.query('''
      SELECT * FROM services
      INNER JOIN users ON users.id = services.user_id
    ''')

    return services

  def get_by_id(self, id: int):
    service = self.DB.execute(f'''
      SELECT * FROM services 
      INNER JOIN users ON users.id = services.user_id
      WHERE services.id = {id}
    ''')

    if not service:
      return None

    return service[0]
 
  def create(self, data: ServiceCreateDto):
    status = None
    try:
      url_req = requests.get(data['url'])
      status = url_req.status_code
    except:
      status = 500

    return self.DB.query(f'''
      INSERT INTO 
        services (title, url, status, user_id)
      VALUES 
        ('{data['title']}', '{data['url']}', {status}, 1)
    ''')
  
  def update(self, data: ServiceUpdateDto):
    return self.DB.query(f'''
      UPDATE services
      SET title = '{data['title']}', url = '{data['url']}'
      WHERE id = {data['id']}
    ''')
  
  def delete(self, id: int):
    return self.DB.query(f'''
      DELETE FROM services
      WHERE id = {id}
    ''')
