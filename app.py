from flask import Flask, request, render_template, render_template_string
import requests
from bs4 import BeautifulSoup 


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       res = ''
       
       return render_template('new.html')

    else:
        print(request.form)
        return '1'
    
    # elif request.method == 'POST':
    #     site = request.form['command']
    #     try:
    #         response = requests.get(site)
    #     except Exception as e:
    #         err = e
    #         return render_template('new.html', err=err)
        
    #     headersDict = response.headers
    #     headerStrings = []
    #     for header in headersDict.keys():
    #         headerStrings.append(': '.join([header, headersDict[header]]))
    #     headers = '\n'.join(headerStrings)
    #     respBody = BeautifulSoup(response.text, 'html.parser').prettify()
    #     return render_template('new.html', result=respBody, headers=render_template_string(headers))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

