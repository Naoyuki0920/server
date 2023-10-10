from flask import Flask
from flask import render_template, request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file'] # type: ignore
    file.save(os.path.join('./static/image', file.filename))
    return f'{file.filename}がアップロードされました'
  else:
    return render_template('upload.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
