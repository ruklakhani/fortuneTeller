from flask import Flask, render_template, request
from random import randint 
import requests

app = Flask(__name__)
API_KEY='b2a6e5d68873b7da1769e863bcf62229'

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
        dogs = " "
    elif memes == "no": 
        dogs = " "
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
        'luckyNumber': luckyNumber,
        'fortune': fortune
    }
    return render_template('results.html', fortunes=fortunes)

@app.route ('/weather')
def weather():
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results_page():
    user_city = request.args.get('city')
    params = {
        'appid': API_KEY,
        'q': user_city, 
        'units': 'Imperial'
    }
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params)
    if not r.status_code == 200:
        print("error")
        return render_template('weather_form.html')
    results = r.json()
    city = results['name']
    degrees = results['main']['temp']
    return render_template('weather_results.html', city=city, degrees=degrees)

if __name__ == '__main__':
    app.run()