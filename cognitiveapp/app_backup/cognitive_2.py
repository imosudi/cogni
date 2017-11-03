import os
import sys
os.environ['NO_PROXY'] = '127.0.0.1'

sys.path.insert(0, '/var/www/clients/client6/web22/cgi-bin/venv/lib/python2.7/site-packages')

from flask import Flask, render_template
#from flask_htpasswd import HtPasswdAuth
from flask_httpauth import HTTPBasicAuth



app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "hello",
    "susan": "bye"
}


"""HTPASSWD = os.path.join(os.path.abspath(os.path.dirname(__file__)), '/var/www/clients/client6/web22/cgi-bin/.htpasswd')

app.config['FLASK_HTPASSWD_PATH'] = HTPASSWD
app.config['FLASK_SECRET'] = 'Hey Hey Kids, secure me!'

htpasswd = HtPasswdAuth(app)"""

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    #return "<h1>It works</h1>"
    #return render_template("test.html")
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
