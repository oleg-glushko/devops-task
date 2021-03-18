from flask import Flask, request
from os import environ
# from flask_cors import CORS
app = Flask(__name__)
# CORS(app)


@app.route('/',methods = ['POST', 'GET'])
def responder():
   if request.method == 'POST':
      body = request.json['body']
      # .data.decode()
   else:
      body = request.args.get('body')

   return f'Method {request.method}, Body "{body}"'


if __name__ == '__main__':
   port = environ.get('FLASK_PORT')
   if (port is not None or port == ""):
     port = '5000'
   app.run(host='0.0.0.0',port=port)
