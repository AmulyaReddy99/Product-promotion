from flask import Flask, render_template, request, url_for, redirect, session
from flask_session import Session
import csv
import database as db
from flask import send_file


sess = Session()
app = Flask(__name__)

categories = ['Financial results','Community stories']

@app.route('/admin')
def admin():
	# SQL = 'SELECT image FROM Articles.articles'
	# db.cur.execute(SQL)
	# row = db.cur.fetchone()[0]
	# file = bytes(row)
	# with open('image.png','wb') as f:
	# 	f.write(file)
	# return send_file('image.png', mimetype='image/png')
	return render_template('admin.html',categories=categories)

@app.route('/')
def index():
	SQL = 'SELECT product_id,category_id,prod_title,description,image,brand,price FROM products'
	db.cur.execute(SQL)
	products = db.cur.fetchall()
	
	return render_template('index.html',categories=categories,products=products)



def validate(email,password):
	SQL = 'SELECT email from users where user="manikya"'
	try:
		result_set = db.cur.execute(SQL)
		if result_set == email:
			session['admin'] = True
	except:
		print('You are not Admin')


@app.route('/login', methods = ['POST'])
def identify_lang():
	email = request.form['email']
	password = request.form['password']
	validate(email,password)
	session['email'] = email
	return redirect(url_for('index'))

@app.route('/logout')
def clear_():
	session.clear()
	return redirect(url_for('index'))


@app.route('/insert',methods=['POST'])
def insert_article():
	title = request.form['title']
	body = request.form['body']
	image = request.form.get('image')
	category_tag = request.form['category_tag']
	
	SQL = 'SELECT category_id FROM categories WHERE category=\''+category_tag+'\''
	db.cur.execute(SQL)
	category_id = db.cur.fetchone()
	if category_id==None:
		SQL = 'INSERT INTO categories (category) VALUES (\''+category_tag+'\')'
		try:
			db.cur.execute(SQL)
			db.con.commit()
		except Exception as e:
			print("ERROR inserting in categories table:",e)
		SQL = 'SELECT category_id FROM categories WHERE category=\''+category_tag+'\''
		db.cur.execute(SQL)
		category_id = db.cur.fetchone()

	brand = request.form['company']
	price = request.form['price']
	SQL = 'INSERT INTO products (category_id,prod_title,description,image,brand,price) VALUES (%s,%s,%s,%s,%s,%s)'
	try:
		db.cur.execute(SQL,(category_id,title,body,image,brand,price))
		db.con.commit()
	except Exception as e:
		print('Failed insertion',e)
	return redirect(url_for('index'))


@app.route('/delete')
def delete_article():
	SQL = 'DELETE FROM TABLE products where product_id=%d'
	db.cur.execute(SQL,request.form['article_id'])


if __name__=='__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug = True, port=5000, host="0.0.0.0")


