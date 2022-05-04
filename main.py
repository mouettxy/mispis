from db.Database import Database
from controllers.AnnouncementController import AnnouncementController
from controllers.ServiceController import ServiceController
from controllers.UserController import UserController

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  db = Database()

  controller = ServiceController(db)

  services = controller.get_all()

  return render_template('pages/index.html', services=services)

if __name__ == '__main__':
  app.run(debug=True)