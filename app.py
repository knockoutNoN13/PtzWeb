from flask import Flask, request, render_template, render_template_string, redirect, url_for
import requests
from bs4 import BeautifulSoup
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':      
       return render_template('new.html')

    else:
        requestDict = request.form.to_dict(flat=False)
        site = requestDict['site'][0]
        headers = {}
        try:
            headName = requestDict['headerName']
            headVal = requestDict['headerValue']
            for i in zip(headName, headVal):
                headers[i[0]] = i[1]
        except:
            pass
        
        if 'reqType' in requestDict.keys():
            print('post')
        return redirect(url_for("home"))
    
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

