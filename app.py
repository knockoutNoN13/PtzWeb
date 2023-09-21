from flask import Flask, request, render_template, render_template_string, redirect, url_for
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        res = ''
        return render_template('home.html', result=render_template_string(res))
    elif request.method == 'POST':
        try:
            site = request.form['in']
            print(site)
            res = os.popen(f'curl {site}').read()
            # res = res.replace('{', '')
            print(res)

        except:
            res = ''
    return render_template('home.html', result=res)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")