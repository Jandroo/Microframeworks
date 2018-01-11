from flask import Flask, request, render_template, session
from random import randint

app = Flask(__name__)
app.secret_key = 'clave'

@app.route('/', methods=['GET','POST'])

def indice():
	
	if request.method == 'POST':
		numero = int(request.form['fname'])
		random = session.get('random', None)

		if(numero > random):
			return render_template('adivinar_template.html', msg="<p>El numero que buscas es MENOR.</p>")
		elif(numero < random):
			return render_template('adivinar_template.html', msg="<p>El numero que buscas es MAYOR.</p>")
		else:
			session['random'] = randint(1,100)
			return render_template('adivinar_template.html', msg="""<h2>Has acertado el numero!!</h2><p>Si quieres jugar de nuevo 
				con otro numero solo tienes que volver a jugar.<p>""")
	else:
		session['random'] = randint(1,100)
		return render_template('adivinar_template.html')
