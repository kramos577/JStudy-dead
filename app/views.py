#   encoding: utf-8
from flask import render_template
#This function takes a template filename and a variable list of template arguments and returns the rendered template, with all the arguments replaced.
#Under the covers, the render_template function invokes the Jinja2 templating engine that is part of the Flask framework. Jinja2 substitutes {{...}}
#blocks with the corresponding values provided as template arguments.

#first line of any file with Japanese = (tab)encoding: utf-16    and then put u'char' everywhere
#all ... are ~     and words with more than one meanign are in an array    and there are no capital letters excpet the pronoun I 　　and　katakana is in hiragana
from app import app
from ch1vocab import ch1V
from ch2vocab import ch2V
from ch3vocab import ch3V
from ch4vocab import ch4V
from ch1hiragana import ch1K
from ch2katakana import ch2K
from ch3kanji import ch3K
from usefulExpr import expr


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')

@app.route('/lessons')
def lessons():
    return render_template("lessons.html",
                           title='Lessons')


#KANJI PAGES
@app.route('/kanji')
def kanji():
    return render_template("kanji.html",
                           title='Kanji')

@app.route('/kanji/hiragana')
def hiragana():
    return render_template("ch1hiragana.html",
                           title='Hiragana',
                           kanji=ch1K)

@app.route('/kanji/katakana')
def katakana():
    return render_template("ch2katakana.html",
                           title='Katakana',
                           kanji=ch2K)

@app.route('/kanji/ch3')
def ch3kanji():
    return render_template("ch3kanji.html",
                           title='Ch3 Kanji',
                           kanji=ch3K)


#VOCAB PAGES
@app.route('/vocab')
def vocab():
    return render_template("vocab.html",
                           title='Vocabulary') #appending is list1 + list2 and just appends in order

@app.route('/vocab/ch1')
def ch1vocab():
    return render_template("ch1vocab.html",
                           title='Ch1 Vocabulary',
                           chap=ch1V)

@app.route('/vocab/ch2')
def ch2vocab():
    return render_template("ch2vocab.html",
                           title='Ch2 Vocabulary',
                           chap=ch2V)
@app.route('/vocab/ch3')
def ch3vocab():
    return render_template("ch3vocab.html",
                           title='Ch3 Vocabulary',
                           chap=ch3V)
@app.route('/vocab/ch4')
def ch4vocab():
    return render_template("ch4vocab.html",
                           title='Ch4 Vocabulary',
                           chap=ch4V)
