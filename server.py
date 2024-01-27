'''Building a server to deploy my website'''
# pylint: disable = W0702
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home_pg():
    '''Function to display index.html'''
    return render_template('./index.html')


@app.route('/<string:page_name>')
def my_html_pages(page_name):
    '''Function to display all .html pages'''
    return render_template(page_name)


def write_data_to_file(data):
    '''function writes the submit_form data in a file.txt'''
    with open('database.txt', mode='a', encoding='utf-8') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email},  |  {subject},  |  {message}')
    return file


def write_data_to_csv(data):
    '''function writes the submit_form data in a file.txt'''
    with open('database.csv', mode='a', encoding='utf-8', newline="") as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
    return csv_writer


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    '''This function prints a message on the front end'''
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_to_csv(data)
            write_data_to_file(data)
            return redirect('./thankyou.html')
        except:
            return 'Data is not saved to Database'
    else:
        return 'Something went wrong while submitting. Try again :('


# @app.route('/works.html')
# def my_works_pg():
#     '''Function to display works.html'''
#     return render_template('./works.html')


# @app.route('/work.html')
# def my_work_pg():
#     '''Function to display work.html'''
#     return render_template('./work.html')


# @app.route('/about.html')
# def about_me_pg():
#     '''Function to display about.html'''
#     return render_template('./about.html')


# @app.route('/contact.html')
# def my_contact_pg():
#     '''Function to display contact.html'''
#     return render_template('./contact.html')
