from db.Database import Database
from controllers.AnnouncementController import AnnouncementController
from controllers.ServiceController import ServiceController, ServiceCreateDto
from controllers.UserController import UserController

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'q7s3FTmXKGuRHvaFHcoreZHDZ4mpEDpu'

@app.route('/')
def index():
  db = Database()
  controller = ServiceController(db)
  services = controller.get_all()

  return render_template('pages/index.html', services=services)

@app.route('/create', methods=('GET', 'POST'))
def create_service():
  if request.method == 'POST':
    title = request.form['title']
    url = request.form['url']

    if not title:
      flash('Пожалуйста, укажите название сервиса', 'danger')
    elif not url:
      flash('Пожалуйста, укажите URL сервиса', 'danger')
    else:
      db = Database()
      controller = ServiceController(db)
      controller.create({ 'title': title, 'url': url })
      
      return redirect(url_for('index')) 

  return render_template('pages/create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit_service(id: int):
  db = Database()
  controller = ServiceController(db)

  service = controller.get_by_id(id)

  if request.method == 'POST':
    title = request.form['title']
    url = request.form['url']

    if not title:
      flash('Пожалуйста, укажите название сервиса', 'danger')
    elif not url:
      flash('Пожалуйста, укажите URL сервиса', 'danger')
    else:
      controller.update({ 'id': id, 'title': title, 'url': url })
      
      return redirect(url_for('index')) 

  return render_template('pages/edit.html', service=service)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
  db = Database()
  controller = ServiceController(db)

  service = controller.get_by_id(id)
  controller.delete(id)

  flash(f'Сервис {service["title"]} был успешно удалён', 'info')

  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)