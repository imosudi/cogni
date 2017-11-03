import os
import sys
sys.path.insert(0, '/var/www/clients/client6/web22/cgi-bin/venv/lib/python2.7/site-packages')

from flask import Flask, render_template
from flask_htpasswd import HtPasswdAuth



app = Flask(__name__)

HTPASSWD = os.path.join(os.path.abspath(os.path.dirname(__file__)), '/var/www/clients/client6/web22/cgi-bin/.htpasswd')

app.config['FLASK_HTPASSWD_PATH'] = HTPASSWD
app.config['FLASK_SECRET'] = 'Hey Hey Kids, secure me!'

htpasswd = HtPasswdAuth(app)



@app.route('/')
@htpasswd.required
def home():
    #return "<h1>It works</h1>"
    return render_template("test.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
