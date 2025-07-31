from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'GKbotz'


if name == "__main__":
    app.run()
