from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_flask():
    return "Hello flask"

@app.route('/new/')
def query_string(greeting = "Hello"):
    query_val = request.args.get('greeting', greeting)
    return "<h1> the greeting is {}. </h1>".format(query_val)

@app.route('/user/')
@app.route('/user/<name>')
def no_query_string(name='Mina'):
    return "<h1> Hello there, {}!!! </h1>".format(name)

    
if __name__ == "__main__":
    app.run(debug=True)
