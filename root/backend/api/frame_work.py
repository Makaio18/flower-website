#Adriel Makaio Villarreal
"""
Frame work for the the indvidual data base holding the html data, and how I am going to populate the infromation
"""
import requests
from flask import Flask, jsonify
import random
import time
import json

class FlowerGen:

    def __init__(self, url, cache_ttl=3600) :
        self.url = url
        self.cache_ttl = cache_ttl
        self.flowers= None
        self.fetched_at = 0
        self.response.json()

    def _fetch_flowers(self) :
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()


    def  _is_cache_stale(self)  :
        return self._self.flowers is None or (time.time() - self._fetched_at) > self.cache_ttl


    def get_all_flowers(self)   :

        if (self.self._is_cache_stale())    :
            self._flowers = self._fetch_flowers()
            self._fetch_at = time.time()
        return self.flowers


    def get_random_flower(self)    :
        return random.choice(self.get_all_flowers())

app = Flask(__name__)
flower_gen = FlowerGen("https://datasets-server.huggingface.co/rows?dataset=jobcher%2Fflower-datasets&config=default&split=train&offset=0&length=100")


@app.route("/api/random-flower")
def random_flower():
    return jsonify(flower_gen.get_random_flower)



# Hi I am just testing if this is making it to my git hub repo



