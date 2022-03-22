from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

boiler = {"boiler":False}

@app.route("/")
def index():
    if boiler["boiler"] == True:
        boiler["boiler"] = False
    else:
        boiler["boiler"] = True
    print(boiler)
    return render_template('index.html', boiler_status=boiler)

@app.route("/boiler", methods=['GET'])
def get_boiler():
    return(jsonify(boiler))

if __name__ == '__main__':
    app.run(host="192.168.1.157")
