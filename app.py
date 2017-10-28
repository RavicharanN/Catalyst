from flask import Flask,render_template,url_for,redirect,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/processSend',methods = ['POST','GET'])
# def processSend():
#     if request.method == "GET":
#         path = request.args.get('path')
#         return path
#     else:
#         path = request.form

@app.route('/send',methods = ['POST','GET'])
def send():
    if request.method == "GET":
        return render_template('send.html')
    else:
        path = request.form['path']
        print(path)
        return path

@app.route('/receive')
def receive():
    return render_template('receive.html')

if __name__ == "__main__":
    app.run(debug=True)
