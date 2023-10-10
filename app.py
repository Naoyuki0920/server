from flask import Flask
from flask import render_template, request
import os

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        number = request.form['number']  # type: ignore
        file = request.files['file']  # type: ignore
        folder_path = os.path.join('./static/image', number)
        if not os.path.exists(folder_path):
            os.makedirs('./static/image')
        file.save(os.path.join(folder_path, file.filename))
        return render_template('finish.html', filename=file.filename)
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
