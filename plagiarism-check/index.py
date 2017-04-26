from flask import Flask
from flask import request
from flask import render_template
import algo

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismDetected = algo.checker(text1, text2)

    if plagiarismDetected is True:
        return "<h1>Plagiarism detected!</h1>"
    else:
        return "<h1>Plagiarism not detected!</h1>"

if __name__ == "__main__":
    app.run()
