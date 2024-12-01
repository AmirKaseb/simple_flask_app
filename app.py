from flask import Flask

app = Flask(__name__)

@app.route('/moustafa')
def hello_world():
    return 'Hello, Amir & moustafa!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
