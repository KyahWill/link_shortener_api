from flask import Flask,request, redirect,Response
import random
import string
app = Flask(__name__)

# Routes
# / = post method with body. Verify if it exists
#   If none, then return Errror 404 with error message
# 
# /<code> = get method. Verify if body contains url

#
#
unique_codes = {}

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

@app.route('/',methods = ['POST'])
def createShortenedLink():
    variable = request.get_json()
    url = variable['url']
    code = get_random_string(6)
    while code in unique_codes.keys():
        code = get_random_string(6)    
    
    unique_codes[code] = url
    return Response(request.base_url + code , 200)

@app.route('/<string:code>')
def redirectShortenedLink(code):
    if code in unique_codes.keys():
        return redirect(unique_codes[code], code=302)
    else:
        return 500