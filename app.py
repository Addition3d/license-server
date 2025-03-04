from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # Your Flask route

if __name__ == '__main__':
    app.run(debug=True)
