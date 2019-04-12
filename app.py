''' attention ici on appelle request et non pas requests (sans "s")'''
from flask import Flask, render_template, url_for, request
import requests
import pandas as pd
import json

# =============================================================================
# darksky
# =============================================================================

ip_key = '33a589c69598f9ec4b5c742140128b05'
ip_url = 'http://api.ipstack.com/62.23.222.136?access_key={}'.format(ip_key)

r = requests.get(ip_url).json()
def_lat = r['latitude']
def_long = r['longitude']


app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        lat = dict(request.form)["lat"]
        long = dict(request.form)["long"]
    else:
        lat = def_lat
        long = def_long
    ds_key = 'f42879e6e8a9232a6a2dd67732dc8709'
    ds_url = 'https://api.darksky.net/forecast/{}/{},{}'.format(ds_key, lat,long)
    weather = requests.get(ds_url).json()
    tomorrow = weather["daily"]["data"][1]["summary"]
    city = weather["timezone"]
    return render_template("index.html", lat = lat, long = long, weather = tomorrow, city = city)

'''
@app.route("/merci", methods=["GET", "POST"])
def merci():
    if request.method == "POST":
        name = dict(request.form)["name"]
        email = dict(request.form)["email"]
        message = dict(request.form)["message"]
    else:
        name = ''
    return render_template("merci.html", var1 = name)


permet de différencier l'ouverture de flask "import flask" (ou name n'est pas "main") d'une application ou flask est le composant principal
'''
if __name__ == "__main__":
    app.run(debug=True)
