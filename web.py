import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
from PIL import Image
import json
import ocr

app = Flask(__name__)

app.config['SECRET_KEY'] = 'HELLO'
app.config['UPLOAD_FOLDER'] = './Tests'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Expense(db.Model):
	expense_id = db.Column(db.Integer, primary_key=True)
	expense_type = db.Column(db.String(50))
	amount = db.Column(db.Integer)
	image = db.Column(db.String(50))
	claim_date = db.Column(db.String(50))
	payment_mode = db.Column(db.String(50))
	approval = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return f"Expense('{self.expense_id}', '{self.expense_type}', '{self.amount}', '{self.claim_date}')"

class Hotel(db.Model):
	expense_id = db.Column(db.Integer)
	hotel_name = db.Column(db.String(50))
	check_in = db.Column(db.String(50), primary_key=True)
	check_out = db.Column(db.String(50))

	def __repr__(self):
		return f"Expense('{self.expense_id}', '{self.hotel_name}', '{self.check_in}', '{self.check_out}')"

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

@app.route("/uploadImage", methods=["POST"])
def uploadImage():
	db.create_all()
	file = Image.open(request.files['file'])
	file.save('Image', 'png')
	x = ocr.detect(file)
	expense = Expense(expense_id=1, expense_type='Hotel bill', amount=x['Amount'], claim_date='02/03/2019', payment_mode='Cash')
	hotel = Hotel(expense_id=1, hotel_name='Shivam', check_in='01/03/2019', check_out='02/03/2019')
	db.session.add(expense)
	db.session.add(hotel)
	db.session.commit()
	y = ocr.pred(x)

	return "Success"

@app.route("/getData/<int:expense_id>")
def getData(expense_id):
	expense = Expense.query.get_or_404(expense_id)
	return render_template('expense.html', expense=expense)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')