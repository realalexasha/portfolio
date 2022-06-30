from flask import Flask, render_template, url_for, send_from_directory, request, redirect
import os
import csv

app = Flask(__name__)

# app.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='favicon.ico'))

def write_to_file(data):
	with open('database.txt', 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email}, {subject}, {message}')
		
def write_to_csv(data):
	with open('database.csv', 'a', newline = '') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter = ';', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/')
def my_home(): 
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	# print(data)
    	try:
    		write_to_csv(data)
    		return redirect('thankyou.html')
    	except:
    		print('didn\'t save to database')
    	else:
    		print('something went wrong')


# @app.route("/index.html")
# def my_home2():
# 	return render_template('index.html')

# @app.route("/works.html")
# def works():
# 	return render_template('index.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')