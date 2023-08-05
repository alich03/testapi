from flask import Flask, request, jsonify, url_for


app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Flask App is ok now  HELLO WORLD! "</h1>"









if __name__ == '__main__':
    app.run()
