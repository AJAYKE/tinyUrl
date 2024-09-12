from datetime import datetime

import requests
from flask import Flask, redirect, request

from mongo import add_url_to_mongo, read_from_mongo
from store_in_redis import get_key_from_redis, set_key_in_redis

app =Flask(__name__)

@app.route("/")
def main():
    return "yo app is running"

@app.route("/generate_short_url", methods = ['GET'])
def generate_short_url():
    longUrl = request.args.get("url")
    response = requests.get('http://127.0.0.1:5000/generate_key')
    if response.status_code == 200:
        shorturl = response.json().get("short_url")
        add_url_to_mongo(short_url=shorturl, long_url=longUrl,user_id=1213,created_at=datetime.utcnow().strftime('%d%m%y%H%M'))
        set_key_in_redis(longUrl,shorturl)
        return {"short_url":shorturl}
    else:
        raise Exception

@app.route("/<url>", methods=['GET'])
def getUrl(url):
    shorturl = url
    try:
        longurl = get_key_from_redis(shorturl)
        return redirect(longurl,code=302)
    except:
        longurl = read_from_mongo(short_url=shorturl)
        set_key_in_redis(longurl,shorturl)
        return redirect(longurl,code=302)
if __name__ == '__main__':
    app.run(port=4000)