# rendering templates

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


@app.route('/new')
def query_string(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)


@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </>'.format(name)


# strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'


@app.route('/temp')
def using_templates():
    return render_template('hello.html', name = "Quan")

@app.route('/table')
def movie_plus():
    movies_dict = {
        'Once upon a time' : 2.12,
        'Dragon Head' : 3.15,
        'Avatar' : 0.9,
        'Coldmind' : 0.86,
        'Frozen 2' : 0.7
    }
    return render_template('table.html',
                            movies=movies_dict,
                            name="Quan")
@app.route('/filters')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('filter_data.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')
                           
# Now the app starts here  

@app.route('/macros')
def jinja_macro():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macros.html',
                           movies=movies_dict)

if __name__ == "__main__":
    app.run(debug=True)
