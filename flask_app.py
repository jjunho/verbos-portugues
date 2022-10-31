from flask import Flask, render_template, request
from port import continuous, future

app = Flask(__name__)


@app.get("/")
def home_get():
    return render_template('index.html')


@app.post("/")
def home_post():
    s = request.form['form_s']
    v = request.form['form_v']
    o = request.form['form_o']
    cont = continuous(s, v, o)
    fut = future(s, v, o)
    return render_template('index.html', cont=cont, fut=fut)
