from __future__ import with_statement
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
      render_template, flash, _app_ctx_stack, send_from_directory
from werkzeug import secure_filename

# configuracion
DEBUG = True
UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('PICOLOR_SETTINGS', silent=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# archivos permitidos
def allowed_file(filename):
   return '.' in filename and \
         filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def show_index():
   return render_template('index.html')

@app.route('/',methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
         return redirect(url_for('show_file',
            filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/show/<filename>')
def show_file(filename):
   image = "http://127.0.0.1:5000/uploads/"+filename
   print image
   return render_template('view_image.html',image=image)

if __name__=='__main__':
   app.run()
