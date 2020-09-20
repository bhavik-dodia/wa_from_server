from urllib.parse import unquote
from automate import send_data
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/automate", methods=['GET', 'POST'])

def response():
    # query = request.values.get('query')
    # query = unquote(query)
    # print(query)
    res = send_data(['Abhishek Doshi', 'Deep Gandhi'], 'query', 'script: image from server')
    return jsonify({"query" : 'query', "response" : res})

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0')