from flask import Flask, render_template, request, url_for, redirect, session
from flask_session import Session
import csv
import database as db
from flask import send_file


sess = Session()
app = Flask(__name__)

categories = ['Financial results', 'Management change updates', 'Insider Trading','Special situations', 'KPI', 'IPO', 'Stars shareholdings', 'Super growth stories', 'Community stories']

@app.route('/admin')
def index():
	# SQL = 'SELECT image FROM Articles.articles'
	# db.cur.execute(SQL)
	# row = db.cur.fetchone()[0]
	# file = bytes(row)
	# with open('image.png','wb') as f:
	# 	f.write(file)
	# return send_file('image.png', mimetype='image/png')
	return render_template('admin.html',categories=categories)


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
	company = request.form['company']
	SQL = 'INSERT INTO Articles.articles (title,body,image,category_tag,company) VALUES (%s,%s,%s,%s,%s)'
	try:
		db.cur.execute(SQL,(title,body,image,category_tag,company))
		db.con.commit()
	except Exception as e:
		print('Failed insertion',e)
	return redirect(url_for('index'))


@app.route('/delete')
def delete_article():
	SQL = 'DELETE FROM TABLE article where ID=%d'
	db.cur.execute(SQL,request.form['article_id'])


if __name__=='__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug = True, port=5000, host="0.0.0.0")


