import os
import tensorflow as tf
import numpy as np
import data_utils
from translate import Transliteration
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
transliteration = Transliteration()

@app.route("/", methods=['GET'])
def main():
  return render_template('index.html')

@app.route("/", methods=['POST'])
def transliterate():
  input = request.form['input']
  output, learned = transliteration.run(input)
  return jsonify({'input': input, 'output': output, 'learned': learned})

if __name__ == "__main__":
#  app.debug = True
  app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

