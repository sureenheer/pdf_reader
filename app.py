import read_pdf as reader
from flask import Flask, request, render_template, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return redirect(request.url)
        file = request.files['pdf']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('read_pdf', filename=file.filename))
    return render_template('index.html')

@app.route('/read/<filename>')
def read_pdf(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    reader.read_pdf(filepath)
    return render_template('controls.html', filename=filename)

@app.route('/pause')
def pause():
    reader.pause()
    return jsonify(success=True)

@app.route('/resume')
def resume():
    reader.resume()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True, port=5501)