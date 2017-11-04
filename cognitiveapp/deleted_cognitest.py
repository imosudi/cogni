from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_script import Manager
from flask_moment import Moment
from flask import send_file
from flask import send_from_directory

from flask_bootstrap import Bootstrap
from flask_wtf import Form

from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required


from markupsafe import Markup # for the wtf form custom class
import pandas as pd
from cStringIO import StringIO
import StringIO
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

#from cube2 import Cube
#from cube2 import Cube
from logic import rubikOperation
from forms import *
from routes import *
from datetime import datetime


#November 4 2017
from sscognitive import WavePlot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
	#return '<h1> Cotta & Cush </h1> '
	form = rubikForm()
	formM = rubikFormM()
	#formM.m.data  = ''
	rubikOp = rubikOperation()
	num = rubikOp.inputNbyNbyN()
	if num > 1 and num < 15:
		cubeletSum = rubikOp.numCubelets()
		FacesCubelets = rubikOp.numFacesCubelets()
		hidden = rubikOp.hiddenCubelets()
		m = rubikOp.nM()
		formM.m.data  = m
	elif num > 14:
		flash ('Provide n (1<n<14) TOO MUCH')
		num = 3
		cubeletSum = 27
		FacesCubelets = 26
		hidden = 1
		m = 1
		formM.m.data  = m
	elif num < 2:
		#flash ('Provide n (1<n<14) ')
		num = 3
		cubeletSum = 27
		FacesCubelets = 26
		hidden = 1
		m = 1
		formM.m.data  = m
	elif num is None:
		flash ('')
		num = 3
		cubeletSum = 27
		FacesCubelets = 26
		hidden = 1
		m = 1
		formM.m.data  = m
	
	
	
	#form = rubikForm()
	#formM = rubikFormM()
	#formM.m.data  = m
	'''if form.validate_on_submit():
					old_n = session.get('n')
					if old_n is None:
						flash('')
					elif old_n >= 1:
						flash ('Provide n more than 1 for nXnXn Rubik\'s Cube ')
					session['n'] = int(form.n.data)
					#form.name.data = ''
					form.n.data = ''
					return redirect(url_for('index'))'''
	#num = session.get('n')
	#if m > 1
	img = StringIO.StringIO()
	np.random.seed(42)
	"""fig = Cube(num, whiteplastic=True)
	fig.render(flat=False).savefig(img, format='png',  dpi=965 )
	img.seek(0)
	plot_url = base64.b64encode(img.getvalue())
	
	fig2 = WavePlot()
	fig2.render.savefig(img, format='png', dpi=965)
	img.seek(0)
	plot_url = base64.b64encode(img.getvalue())"""

	#session['n'] = form.n.data
	#session['cubeletsNum'] = objectCubelets.inputNbyNbyN(n)
	return render_template('index.html', 
		cubeletSum=cubeletSum, plot_url=plot_url,
		FacesCubelets =FacesCubelets, hidden=hidden, 
		num=num, form=form, formM=formM, m=m, current_time=datetime.utcnow())# cubeletsNum=session.get('cubeletsNum'))

	pass


#ref: https://github.com/davidwhogg/MagicCube
#ref: https://stackoverflow.com/questions/646286/python-pil-how-to-write-png-image-to-string
#ref: https://stackoverflow.com/questions/25140826/generate-image-embed-in-flask-with-a-data-uri
#ref: https://stackoverflow.com/questions/34492197/how-to-render-and-return-plot-to-view-in-flask
#ref: http://jinja.pocoo.org/docs/dev/templates/#include
#ref: https://github.com/miguelgrinberg/flasky/issues/79




@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html', current_time=datetime.utcnow()), 500


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', current_time=datetime.utcnow()), 404



''' {{ form.n(class_='cotta_cush', id='cotta_cush') }}
function fillValuesInTextBoxes()
{
    var text = document.getElementById("firsttextbox").value;
    document.getElementById("secondtextbox").value = text;
}'''



if __name__ == '__main__':
    #manager.run()
    app.run(debug=True, host='0.0.0.0')
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
