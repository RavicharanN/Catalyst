from flask import Flask,render_template,url_for,redirect,request
from send import send
from receive import receive
from flask_compress import Compress

app = Flask(__name__)

COMPRESS_MIMEYPES = ['text/html','text/css','text/js']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)

@app.route('/success/<message>')
def success(message):
    return render_template('success.html',message = message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sender',methods=['POST','GET'])
def sender():
    if request.method == "GET":
        return render_template('sender.html')
    else:
        path = request.form['path']
        send(path,9999)
        message = "SentSuccessfully"
        return redirect(url_for('success',message = message))

@app.route('/receiver', methods = ['POST','GET'])
def receiver():
    error = None
    try:
        if request.method == "GET":
            return render_template('receiver.html')
        else:
            ip = request.form['ip']
            receive(ip,9999)
            message = "ReceivedSuccessfully"
            return redirect(url_for('success',message = message))
    except Exception as e:
        error = "IP Invalid or change port"
        return redirect(url_for('index'))
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
    

if __name__ == "__main__":
    app.run(debug=True)
