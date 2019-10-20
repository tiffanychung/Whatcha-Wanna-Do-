from flask import Flask, request, render_template
from app import eb_api_query
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':
        # language = request.form.get('language')
        # framework = request.form['framework']
        radius = request.form.get('radius')
        categories = request.form.get('categories')
        date = request.form.get('date')
        price = request.form.get('price')
        location = request.form.get('location')
        event_list =eb_api_query(date,location, price, radius, categories)
        return render_template('index.html', name = event_list)


        # return '''<h1>The language value is: {}</h1>
        #           <h1>The framework value is: {}</h1>'''.format(language, framework)
    # return '''<form method="POST">
    #               Language: <input type="text" name="language"><br>
    #               Framework: <input type="text" name="framework"><br>
    #               <input type="submit" value="Submit"><br>
    #           </form>'''
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
