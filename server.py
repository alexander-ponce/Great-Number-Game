from flask import Flask, render_template, session, redirect, request
import random  # added render_tempipeplate!
app = Flask(__name__)
app.secret_key="Secret, secret key."                      

@app.route('/')
def index():
    
    if "number" not in session:
        session['number'] = random.randint(1,100)


    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'


if __name__=="__main__":
    app.run(debug=True)                   





