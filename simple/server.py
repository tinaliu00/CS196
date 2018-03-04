from flask import render_template, request, redirect
from simple import app
from simple.forms import Contact

@app.route('/')
@app.route('/home')
def home():
    return render_template('generic.html', title='Home', header='Home', content='Home sweet home.',
    maru='yip')

@app.route('/about')
def about():
    return render_template('generic.html', title='About', header='About the World',
    content='Did you know that most cats are scientifically proven to be cuter than most dogs?',
    cat='meow')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=='GET':
        form = Contact()
        return render_template('form.html', title='Contact', header='Contact', content='Share your thoughts.',
        shibe='bork', form=form)
    elif request.method=='POST':
        form_stuff = request.form
        for key in form_stuff:
            print(key + ": " + form_stuff[key])
        return redirect('/home')
    else:
        return("Error.")
