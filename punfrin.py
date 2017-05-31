from flask import Flask
from flask import render_template, url_for, redirect
from app import twilio_handler

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/pun/', methods=['GET', 'POST'])
def do_pun():
    twilio_handler.send_pun()
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
