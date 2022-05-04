




from db.Database import Database
from controllers.AnnouncementController import AnnouncementController
from controllers.ServiceController import ServiceController
from controllers.UserController import UserController


if __name__ == '__main__':
  db = Database()

  user = UserController(db)
  service = ServiceController(db)
  announcement = AnnouncementController(db)

  print(user.get_all())
  print(service.get_all())
  print(announcement.get_all())