# Main application code for Smart Cart

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Smart Cart!'

if __name__ == '__main__':
    app.run(debug=True)