from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Yuhuuuuuu Docker #2 project is on!'

if __name__ == '__main__':
    app.run()