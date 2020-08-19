from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    port = os.environ.get('PORT') or 5000
    app.run(host='0.0.0.0', port=port, debug=True)