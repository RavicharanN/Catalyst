from flask import Flask,render_template,url_for,redirect,request
from send import send
from receive import receive

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sender',methods=['POST','GET'])
def sender():
    if request.method == "GET":
        return render_template('sender.html')
    else:
        path = request.form['path']
        send(path, raw_input())
        return "Sent!"

@app.route('/receiver', methods = ['POST','GET'])
def receiver():
    if request.method == "GET":
        return render_template('receiver.html')
    else:
        ip = request.form['ip']
        receive(ip, raw_input())
        return "Received!"

if __name__ == "__main__":
    app.run(debug=True)
