from flask import Flask, render_template, request
from random import randint 
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/fortune', methods=['GET','POST'])
def fortune(): 
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def results():
    name = request.args.get('name')
    memes = request.args.get('memes')
    dogs = request.args.get('dogs')
    mood = request.args.get('mood')

rand_color = "%06x" % randint(0, 0xFFFFFF)
lucky_number = randint(100000, 999999)

}


if __name__ == '__main__':
    app.run()