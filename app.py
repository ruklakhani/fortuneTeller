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
    color = request.args.get('color')
    memes = request.args.get('memes')
    dogs = request.args.get('dogs')

    if memes == "sometimes":
        fortune = "Enjoy yourself while you can"
    else:
        if dogs == "pug":
            fortune = "You might feel a little conjested,,, you possibly sick cutie! ;^)"
        elif dogs == "corgi":
            fortune = "You're going to brighten up someone's day!! :^)"
        elif dogs == "italianGreyhound": 
            fortune = "Whatever you're nervous about, it's going to be ok! :^)"
        elif dogs == "husky":
            fortune = "Put on a jacket baybee, it might be chilly. if not,,, you'll just look fresh! "
        else:
            print("dog not found")

    luckyNumber = randint(100000, 999999)

    fortunes = {
        'name': name, 
        'color': color,
        'memes': memes,
        'dogs': dogs,
        'fortune': fortune
    }
    return render_template('results.html', fortunes=fortunes)

if __name__ == '__main__':
    app.run()