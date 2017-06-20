from flask import render_template
#This function takes a template filename and a variable list of template arguments and returns the rendered template, with all the arguments replaced.
#Under the covers, the render_template function invokes the Jinja2 templating engine that is part of the Flask framework. Jinja2 substitutes {{...}}
#blocks with the corresponding values provided as template arguments.
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'The Awesome El Jesso'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/lessons')
def lessons():
    return render_template("lessons.html",
                           title='lessons')

@app.route('/kanji')
def kanji():
    return render_template("kanji.html",
                           title='kanji')

@app.route('/vocab')
def vocab():
    return render_template("vocab.html",
                           title='Vocabulary')
