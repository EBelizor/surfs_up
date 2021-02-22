from flask import Flask

app = Flask(__name__)

# determining the starting point or root
# The forward slash indicates that we want to start at the root of our directory
@app.route('/')
def hello_world():
    return 'Hello World'

