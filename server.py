from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_page(path):
    if '.' not in path:
        file_path = f'{path}.html'
    else:
        file_path = path
    if not os.path.exists(file_path):
        return send_from_directory('.', '404.html'), 404
    return send_from_directory('.', file_path)

@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory('.', '404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)