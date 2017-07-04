#   encoding: utf-8
from flask import render_template
#This function takes a template filename and a variable list of template arguments and returns the rendered template, with all the arguments replaced.
#Under the covers, the render_template function invokes the Jinja2 templating engine that is part of the Flask framework. Jinja2 substitutes {{...}}
#blocks with the corresponding values provided as template arguments.

#first line of any file with Japanese = (tab)encoding: utf-16    and then put u'char' everywhere
#all ... are ~     and words with more than one meanign are in an array    and there are no capital letters excpet the pronoun I 　　and　katakana is in hiragana
from app import app
from ch1vocab import ch1V
from ch3vocab import ch3V
from ch3kanji import ch3K


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')

@app.route('/lessons')
def lessons():
    return render_template("lessons.html",
                           title='Lessons')

@app.route('/kanji')
def kanji():
    return render_template("kanji.html",
                           title='Kanji',
                           kanji=ch3K)


@app.route('/vocab')
def vocab():
    return render_template("vocab.html",
                           title='Vocabulary',
                           chap=ch3V) #appending is list1 + list2 and just appends in order
