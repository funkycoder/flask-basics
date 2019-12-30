# JINJA TEMPLATES
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home_page():
    return "<h1>This is my home page</h1>"

@app.route('/watch')
def top_movies():
    movie_list = ['autopsy of jane doe','neon demon', 'ghost in a shell', 'kong: skull island', 'john wick 2', 'spiderman - homecoming']
    return render_template('movies.html', movies= movie_list, name='Harry')

@app.route('/temp')
def using_templates():
    return render_template('hello.html', name = "Quan")

if __name__ == '__main__':
    app.run(debug=True)