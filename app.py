from flask import Flask, render_template, request
from utils.hashing import hash_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    input_text = ''
    if request.method == 'POST':
        input_text = request.form['text']
        result = hash_text(input_text)
    return render_template('index.html', result=result, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)