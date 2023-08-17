from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['inputText']
    output_text = input_text.upper()
    return render_template('index.html', input_text=input_text, output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
