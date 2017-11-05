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

import time
import io
import base64
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


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

"""from main import main as main_blueprint
app.register_blueprint(main_blueprint)"""

@app.route('/')

def index():
    img = io.BytesIO()
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    plt.figure(1)
    plt.subplot(111)
    ft = np.exp(-t1) * np.cos(2*np.pi*t1)
    ftt = np.exp(-t2) * np.cos(2*np.pi*t2)
    plt.plot(t1, ft, 'bo', t2, ftt, 'k') 
    plt.savefig(img, format='png', dpi=965)
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue())#.decode()

    return render_template("index.html", plot_url=plot_url)

@app.route('/live')
def live_update_demo(blit = False):
    img = io.BytesIO()
    x = np.linspace(0,75., num=200)
    plt.figure()
    plt.subplot(1, 1, 1)

    h1, = plt.plot(x, lw=3)
    plt.text(0.8,1.5, "")
    plt.ylim([-1,1])


    t_start = time.time()
    k=0.
    for i in np.arange(1000):
        h1.set_ydata(np.sin(x/3.+k))
        k+=0.71 #wave frequency
 
        plt.pause(0.000000000001)
        plt.savefig(img, format='png', dpi=965)
	img.seek(0)
	plot_url = base64.b64encode(img.getvalue())#.decode()
	return render_template("index.html", plot_url=plot_url)
 

"""live_update_demo(True)"""

if __name__ == '__main__':
    #manager.run(host='0.0.0.0')
    app.debug = True
    app.run(host='0.0.0.0')
