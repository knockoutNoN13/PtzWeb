from flask import Flask, request, render_template, render_template_string
from os import popen
from bs4 import BeautifulSoup 
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       res = ''
       return render_template('home.html', result=render_template_string(res))
    elif request.method == 'POST':
        try:
            site = request.form['command']
            res = popen(f'curl {site}').read()
            res = BeautifulSoup(res, 'html.parser').prettify()
            print(res)
        except:
            res = ''
        return render_template('home.html', result=render_template_string(res.replace('<!DOCTYPE html>','')))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")