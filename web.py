from flask import Flask, render_template, request
from forms import RegistrationForm, LoginForm
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HELLO'


posts = [
{
	'name':'Kartavya',
	'title':'Expense 1'
},
{
	'name':'XYZ',
	'title':'Expense 2'	
}
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='Title')

# @app.route("/register")
# def register():
# 	form = RegistrationForm()
# 	return render_template('register.html', title='Register', form=form)

# @app.route("/login")
# def register():
# 	form = LoginForm()
# 	return render_template('login.html', title='Login', form=form)

@app.route("/uploadImage")
def uploadImage():
	file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['upload_folder'], filename))	

if __name__ == '__main__':
	app.run(debug=True)