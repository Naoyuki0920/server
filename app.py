from flask import Flask, send_file
from flask import render_template, request
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show/<int:num>', methods=['GET'])
def show(num):
    directory = f'./static/image/{num}'
    files = os.listdir(directory)
    return render_template('show.html', files=files, num = num)

@app.route('/delete/<int:num>/<filename>', methods=['POST'])
def delete_file(num, filename):
    # ファイルを削除
    file_path = os.path.join(f'./static/image/{num}', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return render_template('finish_delete.html', filename=filename)
    else:
        return 'File not found'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        number = request.form['number']  # type: ignore
        file = request.files['file']  # type: ignore
        folder_path = os.path.join('./static/image', number)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file.save(os.path.join(folder_path, file.filename))
        return render_template('finish_upload.html', filename=file.filename)
    else:
        return render_template('upload.html')


@app.route('/confirm_glb/<int:number>', methods=['GET'])
def confirm_glb(number):
    glb_file_path = f'static/image/{number}/{number}.glb'
    return send_file(glb_file_path, as_attachment=True, mimetype='model/gltf-binary')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
