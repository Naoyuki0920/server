from flask import Flask
from flask import render_template, request
import os
import time
from flask import Flask, Response


app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        number = request.form['number']  # type: ignore
        file = request.files['file']  # type: ignore
        folder_path = os.path.join('./static/image', number)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file.save(os.path.join(folder_path, file.filename))
        return render_template('finish.html', filename=file.filename)
    else:
        return render_template('upload.html')


def generate():
    while True:
        time.sleep(60)
        yield f"data: {time.strftime('%H:%M:%S')}\n\n"


@app.route('/events')
def events():
    return Response(generate(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Server-Sent Eventsがよさそう
