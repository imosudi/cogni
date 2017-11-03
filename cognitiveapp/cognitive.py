import os
import sys
#os.environ['NO_PROXY'] = '127.0.0.1'

sys.path.insert(0, '/var/www/clients/client6/web22/cgi-bin/venv/lib/python2.7/site-packages')

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#from models import Role, User



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)


app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///data.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)



@app.route('/')

def index():
    return render_template("index.html")


if __name__ == '__main__':
    #manager.run(host='0.0.0.0')
    app.debug = True
    app.run(host='0.0.0.0')
