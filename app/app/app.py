from flask import Flask, request, render_template, render_template_string, redirect, url_for
import requests
from bs4 import BeautifulSoup
from werkzeug.datastructures import ImmutableMultiDict




app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       headers={}      
       return render_template('home.html', headers=headers)

    else:
        requestDict = request.form.to_dict(flat=False)
        site = requestDict['site'][0]
        body = ''
        try:
            body = requestDict['reqBody'][0]
        except:
            pass
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
                try:
                    response = requests.post(site, headers=headers, data=body)
                except:
                    response = requests.post(site, data=body)
                respHead = response.headers
                respBody = response.text
                for h in respHead.keys():
                    respHead[h] = render_template_string(respHead[h])
                return render_template('home.html', result=respBody, headers=respHead)
            except Exception as e:
                return render_template('home.html', err=str(e), headers={})
        else:
            try:
                try:
                    response = requests.get(site, headers=headers, data=body)
                except:
                    response = requests.get(site, data=body)
                respHead = response.headers
                respBody = response.text
                for h in respHead.keys():
                    respHead[h] = render_template_string(respHead[h])
                return render_template('home.html', result=respBody, headers=respHead)
            except Exception as e:
                return render_template('home.html', err=str(e), headers={}) 

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")

