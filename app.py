from flask import Flask, request, render_template, render_template_string
from subprocess import *
from bs4 import BeautifulSoup 
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       res = ''
       return render_template('home.html', result=render_template_string(res))
    elif request.method == 'POST':
        site = request.form['command']
        resShell = run(f'curl -i {site}', shell = True, text = True, stderr=PIPE, stdout=PIPE)
        res = resShell.stdout
        err = resShell.stderr
        print(res)
        if res:
            headers = res
            res = res
            res = BeautifulSoup(res, 'html.parser').prettify()
        else:
            res = 'No body'
            headers = 'No headers'
        if 'Xferd' in err:
            err=''
        return render_template('home.html', result=res, err=err, headers=render_template_string(headers))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")