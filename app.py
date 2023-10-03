from flask import Flask, request, render_template, render_template_string
import requests
from bs4 import BeautifulSoup 


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       res = ''
       return render_template('home.html', result=res)
    elif request.method == 'POST':
        site = request.form['command']
        try:
            response = requests.get(site)
        except Exception as e:
            err = e
            return render_template('home.html', err=err)
        
        headersDict = response.headers
        headerStrings = []
        for header in headersDict.keys():
            headerStrings.append(': '.join([header, headersDict[header]]))
        headers = '\n'.join(headerStrings)
        respBody = BeautifulSoup(response.text, 'html.parser').prettify()
        print(headers)
        return render_template('home.html', result=respBody, headers=render_template_string(headers))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")








# CURL TYPE

            # site = request.form['command']
        # resShell = run(f'curl -i {site}', shell = True, text = True, stderr=PIPE, stdout=PIPE)
        # res = resShell.stdout
        # err = resShell.stderr
        # print(res)
        # if res:
        #     headers = res.split('<')[0]
        #     res = '<'.join(res.split('<')[1:])
        #     res = BeautifulSoup(res, 'html.parser').prettify()
        # else:
        #     res = 'No body'
        #     headers = 'No headers'
        # if 'Xferd' in err:
        #     err=''