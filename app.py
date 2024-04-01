from flask import Flask, request, redirect, url_for, send_from_directory
from PIL import Image
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = 'static/10.jpg'  # Save the uploaded image as "10.jpg" in the static folder
            file.save(file_path)

            img = Image.open(file_path)
            width, height = img.size
            piece_width = width // 3
            piece_height = height // 3

            for i in range(3):
                for j in range(3):
                    box = (j * piece_width, i * piece_height, (j + 1) * piece_width, (i + 1) * piece_height)
                    piece = img.crop(box)
                    piece.save(f"static/{i * 3 + j + 1}.jpg", format='JPEG')

            return redirect(url_for('show_puzzle'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Submit>
    </form>
    '''

@app.route('/show_puzzle')
def show_puzzle():
    return send_from_directory('templates', 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/<filename>')
def serve_file(filename):
    return send_from_directory('templates', filename)


if __name__ == '__main__':
    app.run(debug=True)
