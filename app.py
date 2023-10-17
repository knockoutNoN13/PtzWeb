from flask import Flask, request, render_template, render_template_string, redirect, url_for
import requests
from bs4 import BeautifulSoup
from werkzeug.datastructures import ImmutableMultiDict
import ast



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
            try:
                response = requests.post(site, headers=headers)
                respHead = response.headers
                respBody = response.text
                
                return render_template('new.html', result=respBody, headers=ast.literal_eval(render_template_string(str(respHead))))
            except Exception as e:
                return render_template('new.html', err=e)
        else:
            try:
                response = requests.get(site, headers=headers)
                respHead = response.headers
                respBody = response.text
                print(respBody, respHead,'hui')
                return render_template('new.html', result=respBody, headers=ast.literal_eval(render_template_string(str(respHead))))
            except Exception as e:
                return render_template('new.html', err=str(e))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

