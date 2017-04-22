from flask import Flask
from flask_mysqldb import MySQL

from flask import render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)

# @app.route('/create_token/<token_name>/<password>')
# def add_token():
# 	if password != "hackru":
# 		return render_template('index.html')
# 	cur = mysql.connection.cursor()
#     cur.execute('''
#     	CREATE TABLE token_name (
#     		id int, 
#     		name varchar(255),
#     		token varchar(255)
# 		);''')
#     # download data from finance api and save as draw.csv
#     # fill data to the database of new token
#     return render_template('priceChart.html')

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute(''' use stockr''') 
    return render_template('index.html')

@app.route('/',methods=['POST'])
def get_token():
	token=request.form['symbol']
	return str("token")
	# cur = mysql.connection.cursor()


if __name__ == "__main__":
	app.run()