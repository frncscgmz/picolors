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
         return redirect(url_for('uploaded_file',
            filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
   return send_from_directory(app.config['UPLOAD_FOLDER'],
         filename)

if __name__=='__main__':
   app.run()
