from flask import Flask,request, redirect,Response
import serverless_wsgi

app = Flask(__name__)
alias_url_dictionary = {}

@app.route('/',methods = ['POST'])
def createShortenedLink():
    req= request.get_json()

    if 'url' not in req.keys():
        return{'message':'Error! Missing URL'}, 404
    url = req['url']
    
    if 'code' not in req.keys():
        return {'message':'Error! Missing Code'}, 404
    alias = req['code']

    if alias in alias_url_dictionary.keys():
        return {'message':'Error! Alias is already made'}, 400
    
    alias_url_dictionary[alias] = url
    message = request.base_url + alias
    return {"message":message}, 200

@app.route('/<string:code>')
def redirectShortenedLink(code):
    if code in alias_url_dictionary.keys():
        return redirect(alias_url_dictionary[code], code=302)
    else:
        return 500
    

import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return serverless_wsgi.handle_request(app,event,context)
