from flask import Flask

app = Flask(__name__)

@app._got_first_request
def before_first_request_func():
    print("This function runs before the first request.")

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
