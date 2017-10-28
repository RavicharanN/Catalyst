from flask import Flask,render_template,url_for,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server')
def server():



@app.route('/client')
def client():


if __name__ == __main__:
    app.run(debug=True)
