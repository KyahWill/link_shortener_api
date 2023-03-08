from flask import Flask,request, redirect,Response

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