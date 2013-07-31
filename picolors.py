from __future__ import with_statement
from flask import Flask, request, session, g, redirect, url_for, abort, \
      render_template, flash, _app_ctx_stack

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('PICOLOR_SETTINGS', silent=True)

@app.route('/')
def show_index():
   return render_template('index.html')

if __name__=='__main__':
   app.run()
