from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
 return "Hello world!"

@app.route('/accounts')
def accounts():
    return some_data

@app.route('/login')
def login():
    return render_template(login.html)

if __name__ == "__main__":
    app.run()